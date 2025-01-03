
# Telegram OSINT Tool - Powered by Yusiqo

![Logo](https://github.com/yusiqo/telegram-osint/blob/main/banner/banner.png?raw=true)

## Description
This tool allows you to perform OSINT (Open Source Intelligence) on Telegram users by fetching detailed information about the target user and their activity across common groups. It uses the **Pyrogram** library to interact with the Telegram API, providing functionalities like retrieving user data, their common groups, and messages from those groups.

## Features
- **User Information**: Retrieve detailed information about any Telegram user including username, name, ID, phone number, bio, status, and more.
- **Common Groups**: Fetch the common groups between the logged-in user and the target user.
- **Messages from Groups**: Fetch messages from common groups that the target user has sent, with the ability to limit the number of messages.
- **Configurable**: Save API credentials, session names, and target user details for easy re-use.
- **Stylish Terminal Output**: Beautiful terminal output with colors and banners for a professional feel.

## Requirements
- Python 3.7 or higher
- Pyrogram library
- Telegram API credentials (API ID and API Hash)
- Dependencies: `pyrogram`, `pyfiglet`, `termcolor`, `json`

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yusiqo/telegram-osint.git
    cd telegram-osint
    ```

2. Install required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up Telegram API credentials:
    - Go to [Telegram Developer](https://my.telegram.org/auth) and create a new application to get your **API ID** and **API Hash**.

4. Configure the tool:
    - When you first run the tool, it will ask for your API credentials (API ID, API Hash) and session name. It will also save these details to `config.json` for future use.

## Usage

### Initial Setup
Run the following command to start the tool and configure it for the first time:
```bash
python osint.py
```
This will prompt you to enter your API credentials, session name, and optionally save them in `config.json`.

### OSINT Operations
After the setup, the tool will allow you to input a target username and the number of messages to fetch from common groups:
```bash
Enter a username for OSINT: Ritalin404
Enter the number of messages to fetch (0: Unlimited): 5
```

The tool will display:
- Your account information (username, name, phone number, etc.)
- The target user's information (username, ID, status, bio, etc.)
- Common groups between you and the target user
- Messages from those groups (if any)

### Example Output
```text
Telegram OSINT Tool - Powered by Pyrogram
--------------------------------------------------
Configuration file found.
API ID: 13428022
Session Name: tg
Do you want to use this configuration? (Y/n): y

Enter a username for OSINT: Ritalin404
Enter the number of messages to fetch (0: Unlimited): 5

[Logged-in Account Information]
Username: kriptroid
Name: Kripto 
ID: 19********
Phone: 9949********

[Target User Information]
Username: Ritalin404
Name: 𝖗𝖔𝖔𝖙@𝖗𝖏𝖙𝖆𝖑𝖏𝖓:~# 
ID: 1487613127
Phone: None
Status: UserStatus.RECENTLY
Bio: None
Bot: No
Verified: No
Restricted: No
Language: None

[Common Groups and Messages]
Group: Group Name (ID: 1234567890)
[2023-12-12 14:32:01] Root: This is a sample message in the group.
.
.
.
.
```

## Contributing
Contributions are welcome! If you would like to contribute, feel free to fork this repository, submit a pull request, or open an issue.

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Write your code or fix the issue.
4. Test thoroughly.
5. Submit a pull request.

## License
This project is licensed under the GNU Lesser General Public License v3.0 (LGPL-3.0).

## Contact
If you have any questions, feel free to open an issue or contact the repository owner directly.

---

*This tool is intended for ethical and educational use. Ensure that you have permission from users before gathering any data from their accounts.*
