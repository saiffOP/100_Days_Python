from tkinter import *
from tkinter import messagebox
import json

BACKGROUND_COLOR = "#B1DDC6"

entered_username = ""
entered_password = ""


# ---------------------------- SAVE ADMIN DATA ------------------------------- #
def add_data():
    global entered_username
    global entered_password
    new_data = {
        "Username": entered_username,
        "Password": entered_password,
    }

    username_length = len(entered_username)
    password_length = len(entered_password)

    if username_length == 0 or password_length == 0:
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


# TODO 1: crete a signup page
# ---------------------------- SIGN UP ------------------------------- #
def signup():
    main_window.destroy()
    window = Tk()
    window.title("SIGN IN")
    window.config(padx=50, pady=50, bg="white")
    global entered_username
    global entered_password

    # Logo
    signup_canvas = Canvas(width=200, height=200)
    bus_img = PhotoImage(file="logo.png")
    signup_canvas.create_image(100, 100, image=bus_img)
    signup_canvas.config(bg="white", highlightthickness=0)
    signup_canvas.grid(column=1, row=0)

    # Labels
    # Username Label
    username_label = Label(text="Username:", bg="white")
    username_label.grid(column=0, row=1)

    # Password Label
    password_label = Label(text="Password:", bg="white")
    password_label.grid(column=0, row=2)

    # Entries
    # Username Entry
    username_entry = Entry(width=35)
    username_entry.grid(column=1, row=1, columnspan=2)

    # Password Entry
    password_entry = Entry(width=35)
    password_entry.grid(column=1, row=2, columnspan=2)

    def save_data():
        global entered_username
        global entered_password
        entered_username = username_entry.get()
        entered_password = password_entry.get()
        add_data()

    # Button
    # Sign up Button

    sign_up_button = Button(text="Sign Up", width=30, command=save_data)
    sign_up_button.grid(column=1, row=4, columnspan=2)

    window.mainloop()


# TODO 2: crete a login page
# ------------------------------- LOGIN ---------------------------------- #
def login():
    main_window.destroy()
    login_window = Tk()
    login_window.title("LOGIN")
    login_window.config(padx=50, pady=50, bg="white")
    global entered_username
    global entered_password

    # Logo
    signup_canvas = Canvas(width=200, height=200)
    bus_img = PhotoImage(file="logo.png")
    signup_canvas.create_image(100, 100, image=bus_img)
    signup_canvas.config(bg="white", highlightthickness=0)
    signup_canvas.grid(column=1, row=0)

    # Labels
    # Username Label
    username_label = Label(text="Username:", bg="white")
    username_label.grid(column=0, row=1)

    # Password Label
    password_label = Label(text="Password:", bg="white")
    password_label.grid(column=0, row=2)

    # Entries
    # Username Entry
    username_entry = Entry(width=35)
    username_entry.grid(column=1, row=1, columnspan=2)

    # Password Entry
    password_entry = Entry(width=35)
    password_entry.grid(column=1, row=2, columnspan=2)

    def check_credentials():
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")
        else:
            user_data = data["Username"]
            pass_data = data["Password"]
        username = username_entry.get()
        password = password_entry.get()
        # Check the entered credentials against saved data, e.g., in a file or database
        if username == user_data and password == pass_data:
            messagebox.showinfo(message="Login Successful")
        else:
            messagebox.showinfo(message="Login Failed")

    # Button
    # Sign up Button

    log_in_button = Button(text="Login", width=30, command=check_credentials)
    log_in_button.grid(column=1, row=4, columnspan=2)

    login_window.mainloop()


# TODO 3: create a main window
# ---------------------------- MAIN WINDOW ------------------------------- #
main_window = Tk()
main_window.title("B.E.S.T BUS BOOKING SYSTEM")
main_window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="card_front.png")
canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 50, text="B.E.S.T BUS BOOKING SYSTEM",
                                font=("Times New Roman", 36, "bold"), fill=BACKGROUND_COLOR)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.pack()

login_button = Button(text="Login", bg=BACKGROUND_COLOR, height=2, width=30, highlightthickness=0, command=login)
canvas.create_window(400, 150, window=login_button)

signup_button = Button(text="Sign Up", bg=BACKGROUND_COLOR, height=2, width=30, highlightthickness=0, command=signup)
canvas.create_window(400, 263, window=signup_button)

main_window.mainloop()



