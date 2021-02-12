# Password Manager

## Project Description
This Password Manager is a desktop GUI application built with Python’s **Tkinter** library. It helps you:
1. Generate a secure, random 16-character password (letters, digits, punctuation).  
2. Automatically copy the generated password to your clipboard.  
3. Save website, email/username, and password entries to a local text file (`password_manager.txt`) with a confirmation dialog.

## Features
- **Secure Password Generation**: Random mix of uppercase/lowercase letters, digits, and symbols.  
- **Clipboard Copy**: Generated passwords are auto-copied for easy pasting.  
- **Data Persistence**: Stores credentials (website, email/username, password) in `./assets/password_manager.txt`.  
- **Input Validation**: Alerts you if any field is empty, and asks for confirmation before saving.  
- **Clear-on-Save**: Clears the input fields after a successful save to streamline multiple entries.

## Prerequisites
- **Python 3.x**  
- **Tkinter** (included with most Python installations)  
- **pyperclip** (for clipboard functionality)  
  ```bash
  pip install pyperclip
  ```

## Installation

1. **Clone or download** this repository to your local machine.  
2. **Install dependencies** (if needed):
   ```bash
   pip install pyperclip
   ```

## How to Run

1. Open a terminal or command prompt and navigate to the project directory (where `main.py` resides).  
2. Launch the application:
   ```bash
   python main.py
   ```
3. The password manager window will open.

## Usage

1. **Website**: Enter the site name or URL.  
2. **Email/Username**: Enter your login email or username.  
3. **Generate Password**: Click **Generate Password** to fill and copy a secure password.  
4. **Store Login Info**: Click **Store Login Info**. Confirm the details, and they’ll be appended to `./assets/password_manager.txt`.  
5. The fields will clear, ready for a new entry.

## Example

![Password Manager Demo](./screenshots/demo.gif)

- After clicking **Generate Password**, the password field populates and copies to clipboard.  
- On **Store Login Info**, a confirmation appears, then the data is saved.

## Project Structure

```
Password Manager/
├── assets/
│   ├── logo.png                     # App logo displayed in GUI
│   └── password_manager.txt         # Stored credentials (created/appended)
├── main.py                          # Tkinter GUI and logic for generating/saving passwords
├── LICENSE                          # MIT License
└── .gitignore                       # Common ignores (e.g., __pycache__)
```

## License
This project is licensed under the [MIT License](LICENSE).

## Author
- **Ivis Perdomo** ([ivyper](https://github.com/ivyper))
