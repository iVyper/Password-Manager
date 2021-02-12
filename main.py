"""
Password Manager

This script creates a GUI application using Tkinter to:
1. Generate secure random passwords.
2. Copy generated passwords to the clipboard.
3. Save website, email/username, and password entries to a text file.
"""

from tkinter import *
from tkinter import messagebox

import random
import string
import pyperclip

FONT = ("Helvetica", 16)

def generate_pass():
    """
    Build a 16-character password from letters, digits, and punctuation.
    Copy it to the clipboard and display it in the password field.
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
    Validate inputs, confirm with the user, and append the data to a text file.
    Clears the input fields upon successful save.
    """
    website = website_input.get()
    email = email_user_input.get()
    password = password_input.get()

    # Ensure no field is empty
    if website == "" or email == "" or password == "":
        messagebox.showerror("Empty Field Error", "Please fill all the fields, then try again.")
    else:
        # Show a confirmation dialog
        confirmation = messagebox.askokcancel("Confirm",f"These are the details entered:\n\n"
                                               f"Website: {website}\n"
                                               f"Email/Username: {email}\n"
                                               f"Password: {password}\n\n"
                                                f"Would you like to continue?\n")

        if confirmation:
            # Append to file
            with open(file="./assets/password_manager.txt", mode="a") as f:
                account_info = f"{website} | {email} | {password}\n"
                f.write(account_info)

            # Clear inputs after saving
            website_input.delete(0, END)
            email_user_input.delete(0, END)
            password_input.delete(0, END)



window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

# Logo/Image at the top
logo = Canvas(window, width = 200, height = 200)
logo_image = PhotoImage(file = "./assets/logo.png")
logo.create_image(100,100, image=logo_image)
logo.grid(row = 0, column = 1)

# Website label & entry
website_label = Label(window, text = "Website:")
website_label.config(font = FONT)
website_label.grid(row = 1, column = 0)

website_input = Entry(window)
website_input.config(font = FONT, width = 35)
website_input.grid(row = 1, column = 1, columnspan = 2, sticky= W)
website_input.focus()

# Email/Username label & entry
email_user_label = Label(window, text = "Email/Username:")
email_user_label.config(font = FONT)
email_user_label.grid(row = 2, column = 0)

email_user_input = Entry(window)
email_user_input.config(font = FONT, width = 35)
email_user_input.grid(row = 2, column = 1, columnspan = 2, sticky= W)

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