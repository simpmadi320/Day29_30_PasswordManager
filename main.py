from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

DEFAULT_EMAIL = "madison_simpson@outlook.com"

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def get_password():
    try:
        with open("password.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message=f"The file could not be found")
    else:
        try:
            username_e.delete(0, END)
            username_e.insert(0, data[website_e.get()]["email"])
            password_e.delete(0, END)
            password_e.insert(0, data[website_e.get()]["password"])
        except KeyError as error_message:
            messagebox.showinfo(title="ERROR", message=f"The website {error_message} could not be found")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_e.delete(0, END)
    password_e.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    web = website_e.get()
    user = username_e.get()
    password = password_e.get()

    # For Json
    new_data = {
        web: {
            "email": user,
            "password": password
        }
    }

    if len(web) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Please make sure all fields are filled")
    else:
        try:
            with open("passwords.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                #Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            data = new_data

        with open("passwords.json", "w") as data_file:
            # Saving updated data
            json.dump(data, data_file, indent=4)
            website_e.delete(0, END)
            password_e.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Row 1
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Row 2
website_l = Label(text="Website")
website_l.grid(column=0, row=1)

website_e = Entry(width=33)
website_e.focus()
website_e.grid(column=1, row=1)

search_b = Button(text="Search", width=14, command=get_password)
search_b.grid(column=2, row=1)

# Row 3
username_l = Label(text="Email/Username:")
username_l.grid(column=0, row=2)

username_e = Entry(width=52)
username_e.insert(0, DEFAULT_EMAIL)
username_e.grid(column=1, row=2, columnspan=2)

# Row 4
password_l = Label(text="Password:")
password_l.grid(column=0, row=3)

password_e = Entry(width=33)
password_e.grid(column=1, row=3)

password_b = Button(text="Generate Password", command=generate_password)
password_b.grid(column=2, row=3)

# Row 5
add_b = Button(text="Add", width=44, command=add_password)
add_b.grid(column=1, row=4, columnspan=2)

window.mainloop()
