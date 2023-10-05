from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


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


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    entered_web = web_entry.get()
    entered_email = email_entry.get()
    entered_pass = password_entry.get()

    web_length = len(entered_web)
    pass_length = len(entered_pass)

    if web_length == 0 or pass_length == 0:
        messagebox.showinfo(message="Please don't leave  any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=entered_web, message=f"These are the details you Entered: \n"
                                                                  f"Email: {entered_email}\nPassword: {entered_pass}\n"
                                                                  f"Is it ok t save?")
        if is_ok:
            data = open("data.txt", mode="a")
            data.write(f"{entered_web} | {entered_email} | {entered_pass}\n")
            data.close()
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
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
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

# Add Button
add_button = Button(text="Add", width=36, command=add_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
