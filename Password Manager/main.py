from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(END, password)

    pyperclip.copy(password)


# ---------------------------- SEARCH DATA ------------------------------- #
def search_data():
    try:
        with open("data.json", "r") as data_file:
            passwords = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        entered_web = web_entry.get().title()
        if len(entered_web) == 0:
            messagebox.showinfo(message="Please enter website name!")
        else:
            if entered_web in passwords:
                web_email = passwords[entered_web]["email"]
                web_pass = passwords[entered_web]["password"]
                messagebox.showinfo(title=entered_web, message=f"Email: {web_email}\nPassword: {web_pass}")
            else:
                messagebox.showinfo(title="Error", message=f"No Details for {entered_web} exists.")
                web_entry.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    entered_web = web_entry.get()
    entered_email = email_entry.get()
    entered_pass = password_entry.get()

    new_data = {
        entered_web.title(): {
            "email": entered_email,
            "password": entered_pass,
        }
    }

    web_length = len(entered_web)
    pass_length = len(entered_pass)

    if web_length == 0 or pass_length == 0:
        messagebox.showinfo(message="Please don't leave  any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

# LABELS

# Website Label
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

# Email label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

# Password Label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries

# Website Entry
web_entry = Entry(width=32)
web_entry.grid(column=1, row=1, sticky="W")
web_entry.focus()

# Email Entry
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(END, "saifshirgaonkar1786@gmail.com")

# Password Entry
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, sticky="W")

# BUTTONS

# Generate Password Button
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=3, sticky="EW")

# Search Button
search_button = Button(text="Search", command=search_data)
search_button.grid(column=2, row=1, sticky="EW")

# Add Button
add_button = Button(text="Add", width=36, command=add_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
