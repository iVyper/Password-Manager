"""
Password Manager

This script provides a Tkinter-based GUI to:
1. Search stored account credentials by website.
2. Generate secure random passwords and copy them to the clipboard.
3. Save new credentials (website, username, password) to a JSON file.
"""

from tkinter import *
from tkinter import messagebox

import json
import random
import string
import pyperclip

FONT = ("Helvetica", 16)

# ---------------------------- SEARCH FUNCTION ------------------------------- #
def search():
    """
    Look up the entered website in the JSON data file.
    If found, display the stored username and password in an info dialog.
    If not found (or file missing), show an appropriate error message.
    """
    search_website = website_input.get()

    try:
        accounts = json.load(open("./assets/password_manager.json", "r"))

        if search_website in accounts:
            messagebox.showinfo(title=f"Account Info for {search_website}", message=f"Email/Username:\n"
                                                                                    f"{accounts[search_website]['username']}\n\n"
                                                                                    f"Password:\n"
                                                                                    f"{accounts[search_website]['password']}")
        else:
            messagebox.showinfo("Account Not Found",
                                "Sorry, there is no available account info for the website provided.")


    except FileNotFoundError:
        messagebox.showerror("File Not Found", "Sorry, there is no file with your accounts available.\n"
                                           "Add an account to get started.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    """
    Create a 16-character password mixing letters, digits, and punctuation.
    Copy it to the clipboard and display it in the password entry field.
    """
    generated_pass = ""
    for random_char in range(16):
        character_choice = random.randint(1,3)
        if character_choice == 1:
            generated_pass += random.choice(string.ascii_letters)
        elif character_choice == 2:
            generated_pass += random.choice(string.digits)
        else:
            generated_pass += random.choice(string.punctuation)

    # Copy to clipboard for easy pasting
    pyperclip.copy(generated_pass)
    # Display inside the Entry widget
    generated_pass = StringVar(window, generated_pass)
    password_input.config(textvariable=generated_pass)


def store_info():
    """
    Validate that all fields are filled, then save the credentials into a JSON file.
    - On first save, create the JSON file.
    - On subsequent saves, load existing data and update it.
    Clears input fields after saving.
    """
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    account = {
        website: {
        'username': username,
        'password': password,
        },
    }

    # Ensure no field is empty
    if website == "" or username == "" or password == "":
        messagebox.showinfo("Cannot add Account", "Please fill all the fields, then try again.")
    else:
        try:
            with open(file="./assets/password_manager.json", mode="r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open(file="./assets/password_manager.json", mode="w") as f:
                json.dump(account, f, indent=4)
        else:
            # Merge new entry and write back to file
            data.update(account)
            with open(file="./assets/password_manager.json", mode="w") as f:
                json.dump(data, f, indent=4)
        finally:
            # Clear inputs after saving
            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

# Logo/Image at the top
logo = Canvas(window, width = 200, height = 200)
logo_image = PhotoImage(file = "./assets/logo.png")
logo.create_image(100,100, image=logo_image)
logo.grid(row = 0, column = 1)

# Website label, entry, and search button
website_label = Label(window, text = "Website:")
website_label.config(font = FONT)
website_label.grid(row = 1, column = 0)

website_input = Entry(window)
website_input.config(font = FONT, width = 21)
website_input.grid(row = 1, column = 1, columnspan = 2, sticky= W)
website_input.focus()

search_button = Button(window, text = "Search", command=search, width = 14)
search_button.config(font = FONT)
search_button.grid(row = 1, column = 2)

# Email/Username label & entry
username_label = Label(window, text ="Email/Username:")
username_label.config(font = FONT)
username_label.grid(row = 2, column = 0)

username_input = Entry(window)
username_input.config(font = FONT, width = 35)
username_input.grid(row = 2, column = 1, columnspan = 2, sticky= W)

# Password label & entry
password_label = Label(window, text = "Password:")
password_label.config(font = FONT)
password_label.grid(row = 3, column = 0)

password_input = Entry(window)
password_input.config(font = FONT, width = 21)
password_input.grid(row = 3, column = 1, sticky= W)

# Generate Password button
generate_pass_button = Button(window, text="Generate Password", command=generate_pass, width=14)
generate_pass_button.config(font = FONT)
generate_pass_button.grid(row = 3, column = 2)

# Store Login Info button
store_info_button = Button(window, text="Store Login Info", command=store_info, width=36)
store_info_button.config(font = FONT)
store_info_button.grid(row = 4, column = 1, columnspan = 2, sticky= W)

window.mainloop()