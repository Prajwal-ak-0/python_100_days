# import tkinter
#
# window = tkinter.Tk()
# window.title("HUI Programme")
# window.minsize(500,300)
#
#
# def onClick():
#     label = tkinter.Label(text=input.get(), font=("Arial", 24, "bold"))
#     label.pack()
#
#
# input = tkinter.Entry()
# input.pack()
#
# btn = tkinter.Button(text="CLICK HERE",command=onClick)
# btn.pack()
#
# window.mainloop()

from tkinter import *
import random
import string
import json
from tkinter import messagebox

window = Tk()
window.title = "Password Manager"
window.minsize(500, 300)
window.config(padx=50, pady=20)


def generate_password():
    length = 15

    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure at least one character from each set
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Generate the rest of the password
    remaining_length = length - len(password)
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    password.extend(random.choice(all_characters) for _ in range(remaining_length))

    # Shuffle the password to make it more secure
    random.shuffle(password)

    # Convert the list to a string
    secure_password = ''.join(password)

    password_entry.insert(0, secure_password)


def save_credentials():
    site = website_entry.get()
    mail = email_entry.get()
    password = password_entry.get()

    json_data = {
        site: {
            "email": mail,
            "password": password
        }
    }

    if len(site) == 0 or len(mail) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # Writing Json File
        file = open("data.json", "w")
        json.dump(json_data, file, indent=4)

        # Reading Json File
        file = open("data.json", "r")
        data = json.load(file)
        print(data)

        # Updating Json File
        data.update(json_data)
        file = open("data.json", "w")
        json.dump(data, file, indent=4)

        file.close()
        website_entry.delete(0, END)
        password_entry.delete(0, END)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.config(padx=20, pady=10)
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.config(padx=25, pady=10)
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.config(pady=10)
password_label.grid(row=3, column=0)

website_entry = Entry(width=52)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=52)
email_entry.insert(0, "prajwalhassan7@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.config(width=14)
generate_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=40, command=save_credentials)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
