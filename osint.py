import os
import json
from pyrogram import Client
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message
from pyfiglet import figlet_format
from termcolor import colored

CONFIG_FILE = "config.json"

def print_banner():
    banner = figlet_format("Telegram OSINT")
    print(colored(banner, "cyan"))
    print(colored("Telegram OSINT Tool - Powered by Yusiqo", "yellow"))
    print(colored("-" * 50, "green"))

def load_config():
    """Load configuration from the file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def save_config(api_id, api_hash, session_name, last_target=None):
    """Save configuration to the file."""
    config_data = {
        "api_id": api_id,
        "api_hash": api_hash,
        "session_name": session_name
    }
    if last_target:
        config_data["last_target"] = last_target
    with open(CONFIG_FILE, "w") as f:
        json.dump(config_data, f, indent=4)
    print(colored("Configuration saved to config.json.", "green"))

def get_config_or_ask():
    """Retrieve API details from the config file or prompt the user."""
    config = load_config()
    if config:
        print(colored("Configuration file found.", "yellow"))
        print(colored(f"API ID: {config['api_id']}", "cyan"))
        print(colored(f"Session Name: {config['session_name']}", "cyan"))
        if "last_target" in config:
            print(colored(f"Last Target: {config['last_target']}", "cyan"))
        use_config = input(colored("Do you want to use this configuration? (Y/n): ", "green")).strip().lower()
        if use_config in ["y", "yes", ""]:
            return config
    print(colored("Please provide your API details.", "yellow"))
    api_id = input(colored("API ID: ", "cyan"))
    api_hash = input(colored("API Hash: ", "cyan"))
    session_name = input(colored("Session Name: ", "cyan"))
    save_config(api_id, api_hash, session_name)
    return {"api_id": api_id, "api_hash": api_hash, "session_name": session_name}

async def osint_user_and_messages(nickname, message_limit, client):
    """Retrieve target user's information and messages."""
    try:
        my_info = await client.get_me()
        print(colored("\n[Logged-in Account Information]", "magenta"))
        print(colored(f"Username: {my_info.username or 'None'}", "cyan"))
        print(colored(f"Name: {my_info.first_name} {my_info.last_name or ''}", "cyan"))
        print(colored(f"ID: {my_info.id}", "cyan"))
        print(colored(f"Phone: {my_info.phone_number or 'None'}\n", "cyan"))

        user = await client.get_users(nickname)
        print(colored("[Target User Information]", "red"))
        print(colored(f"Username: {user.username or 'None'}", "yellow"))
        print(colored(f"Name: {user.first_name} {user.last_name or ''}", "yellow"))
        print(colored(f"ID: {user.id}", "yellow"))
        print(colored(f"Phone: {user.phone_number or 'None'}", "yellow"))
        print(colored(f"Status: {user.status or 'None'}", "yellow"))
        user_bio = getattr(user, 'bio', None)
        print(colored(f"Bio: {user_bio or 'None'}", "yellow"))
        print(colored(f"Bot: {'Yes' if user.is_bot else 'No'}", "yellow"))
        print(colored(f"Verified: {'Yes' if user.is_verified else 'No'}", "yellow"))
        print(colored(f"Restricted: {'Yes' if user.is_restricted else 'No'}", "yellow"))
        print(colored(f"Language: {user.language_code or 'None'}\n", "yellow"))

        print(colored("[Common Groups and Messages]", "blue"))
        try:
            common_chats = await client.get_common_chats(user.id)
            for chat in common_chats:
                print(colored(f"\nGroup: {chat.title} (ID: {chat.id})", "green"))

                count = 0
                async for message in client.get_chat_history(chat.id, limit=400):
                    if message.from_user and message.from_user.id == user.id:
                        sender_name = message.from_user.first_name or "Unknown"
                        print(colored(f"[{message.date}] {sender_name}: {message.text or '[Media/File]'}", "white"))
                        count += 1
                        if message_limit > 0 and count >= message_limit:
                            break
        except Exception as e:
            print(colored(f"Error while retrieving common groups: {e}", "red"))

    except PeerIdInvalid:
        print(colored("User not found or access denied.", "red"))
    except Exception as e:
        print(colored(f"Error: {e}", "red"))

async def main():
    os.system("clear" if os.name == "posix" else "cls")
    print_banner()

    config = get_config_or_ask()
    app = Client(config["session_name"], api_id=config["api_id"], api_hash=config["api_hash"])

    async with app:
        if "last_target" in config:
            print(colored(f"Previous target: {config['last_target']}", "cyan"))
            reuse_last = input(colored("Do you want to reuse the last target? (Y/n): ", "green")).strip().lower()
            if reuse_last in ["y", "yes", ""]:
                nickname = config["last_target"]
            else:
                nickname = input(colored("Enter a new username for OSINT: ", "green"))
        else:
            nickname = input(colored("Enter a username for OSINT: ", "green"))

        message_limit = int(input(colored("Enter the number of messages to fetch (0: Unlimited): ", "green")))
        await osint_user_and_messages(nickname, message_limit, app)

        save_config(config["api_id"], config["api_hash"], config["session_name"], last_target=nickname)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
