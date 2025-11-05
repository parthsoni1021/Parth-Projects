
# write: json.dump()
# read : json.load()
# update: json.update()

from tkinter import *
from tkinter import messagebox  # This is not a class, so wasn't imported in *
import random
import pyperclip
import json

#----------------------------------Generate Password-------------------------------------#
def password_generator():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] 

    a = 6
    b = 4
    c = 5

    d = random.choices(letters, k=a)  #returns a list
    e = random.choices(numbers, k=b)
    f = random.choices(symbols, k=c)

    concat = d+e+f
    random.shuffle(concat)
    password = "".join(concat)    #join keyword is good

    pass_input.insert(0,password)
    pyperclip.copy(password)


#----------------------------------Save Password-------------------------------------#


def add_to_cred_manager():
    website_to_save = web_input.get()
    email_to_save = email_input.get()
    password_to_save = pass_input.get()
    
    new_data = {
        website_to_save:{
            'email': email_to_save,
            'password': password_to_save,
        }
    }

    is_filled = len(website_to_save)>0 and len(password_to_save)>0
    if not is_filled:
        messagebox.showinfo(title='Invalid', message="Please don't leave the entries blank")
    else:
        try:
            with open('data.json', 'r') as f:   
                # Reading old data
                data = json.load(f)    # load methods converts the json data into python dict
        except FileNotFoundError:
            with open('data.json', 'w') as f:
                json.dump(new_data, f, indent=4)
        else:    
            # Updating old data with new data
            data.update(new_data)
            
            # Saving updated data
            with open('data.json', 'w') as g:    
                json.dump(data, g, indent=4)
        finally:
            clear_input_bar()
    
def clear_input_bar():
    web_input.delete(0,END)
    pass_input.delete(0,END)


def search():
    
    website_name = web_input.get()
    try:
        with open('data.json') as data_file:
            data_dict = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message=f'No data file found')
    else:    
        if website_name in data_dict:
            output = f'Username: {data_dict[website_name]['email']} \nPassword: {data_dict[website_name]['password']}'
            messagebox.showinfo(title='Search Result', message=output)
        else:
            messagebox.showinfo(title='Error', message=f'Website name {website_name} not found')

#----------------------------------UI Setup-------------------------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
image_logo = PhotoImage(file=r"C:\Users\Parth Soni\OneDrive - IIT Delhi\Documents\Python\100_projects_in_100_days\Day29\logo.png")
canvas.create_image(100, 100, image=image_logo)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:  ").grid(row=1, column=0, sticky='e', pady=5)

web_input = Entry(width=30)
web_input.grid(row=1, column=1, columnspan=1, sticky='w', pady=5)
web_input.focus()

email_label = Label(text="Email/Username:  ").grid(row=2, column=0, sticky='e')

email_input = Entry(width=40)
email_input.grid(row=2, column=1, columnspan=2, sticky='w')
email_input.insert(0,'parthsoni@gmail.com')   # Pre load the email

pass_label = Label(text="Password:  ").grid(row=3, column=0, sticky='e')

pass_input = Entry(width=30)
pass_input.grid(row=3, column=1, sticky='w')

pass_button = Button(text="Generate Password", command=password_generator).grid(row=3, column=2, sticky='w', pady=5)
search_button = Button(text="Search", command=search).grid(row=1, column=2, sticky='w', pady=5)

add_button = Button(text="Add", width=20, command=add_to_cred_manager).grid(row=4, column=1, columnspan=2, sticky='w')

window.mainloop()