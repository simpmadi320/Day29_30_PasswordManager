from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

DEFAULT_EMAIL = "madison_simpson@outlook.com"

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

    if len(web) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Please make sure all fields are filled")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {user}\n"
                                                      f"Password: {password}\nIs it ok to save?")
        if is_ok:
            with open("passwords.txt", "a") as data_file:
                data_file.write(f"{web} | {user} | {password}\r")
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

website_e = Entry(width=52)
website_e.focus()
website_e.grid(column=1, row=1, columnspan=2)

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
