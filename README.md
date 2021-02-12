# Password Manager

## Project Description
Password Manager is a desktop GUI application built with Python’s `tkinter` that helps you securely generate, store, and retrieve website login credentials. It generates strong random passwords, copies them to your clipboard, and saves your data in a structured JSON file (`password_manager.json`) instead of a plain text file.

## Features
- **Generate Secure Passwords**  
  - Random mix of letters, digits, and symbols  
  - Configurable length and complexity  
  - One-click copy to clipboard via `pyperclip`  
- **Store Credentials**  
  - Save website name, email/username, and password in `assets/password_manager.json`  
  - Data persists between sessions  
- **Search & Retrieve**  
  - Look up saved credentials by website name  
  - Pop-up alerts for found or missing entries  
- **Friendly GUI**  
  - Built with `tkinter` for a simple, intuitive interface  
  - Input validation and error handling with message boxes  

## Prerequisites
- **Python 3.x**  
- **Required Packages**  
  ```bash
  pip install pyperclip
  ```

## Installation
1. **Clone or download** this repository.  
2. **Install dependencies**:  
   ```bash
   pip install pyperclip
   ```
3. **Ensure the data folder exists**:  
   - `assets/password_manager.json` will be created automatically on first run.

## How to Run
1. Open a terminal and navigate to the project root (where `main.py` resides).  
2. Launch the application:
   ```bash
   python main.py
   ```
3. Use the GUI to:
   - Enter a website, your email/username, and either paste or generate a password.  
   - Click **Generate Password** to create & copy a strong password.  
   - Click **Store Login Info** to save your entry.  
   - Use the **Search** button to retrieve credentials for a specific website.

## Demo
![Password Generator Demo](./screenshots/demo.gif)

## Application Layout
| Field               | Description                              |
|---------------------|------------------------------------------|
| Website             | The site or service name (e.g., “Gmail”) |
| Email/Username      | Your login email or user handle          |
| Password            | Your password (auto-generated or custom) |
| Generate Password   | Creates a new random password            |
| Store Login Info    | Saves entry to `password_manager.json`   |
| Search              | Finds and displays stored credentials    |

## Data Storage
All credentials are stored in `assets/password_manager.json` in the form:
```json
{
  "example.com": {
    "email": "user@example.com",
    "password": "Ab#3xY9!"
  },
  "another-site.org": {
    "email": "me@another.org",
    "password": "X7!kLp#2"
  }
}
```

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Author
- **Ivis Perdomo** ([ivyper](https://github.com/ivyper))