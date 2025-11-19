from tkinter import * 
from PIL import Image, ImageTk

PINK = '#e2979c'   #colorhunt.co
RED = '#e7305b'
GREEN = '#9bdeac'
BLUE = '#0000FF'
YELLOW = '#f7f5dd'
#--------------------------------- PASSWORD GENERATOR---------------------------------

#--------------------------------- SAVE PASSWORD ---------------------------------

#--------------------------------- UI SETUP ---------------------------------
root = Tk()
root.geometry('500x400')    # x, not *. passed in ' '
root.title('Password Manager')
root.config(padx=22, pady=22)

def get_coordinates(event):
    x, y = event.x, event.y
    print(f"Coordinates: ({x}, {y})")

canvas = Canvas(height=200, width=200, highlightthickness=0, bd=0, bg=PINK)
# Try to load the logo using tkinter's PhotoImage first. Some Tk builds can't read certain PNG encodings, so fall back to Pillow (PIL) if needed.
try:
	image_logo = PhotoImage(file='logo.png')
except Exception:
	# Using ImageTk pillow lets us support a wider range of PNG/JPEG formats.
	
	img = Image.open('logo.png')
	image_logo = ImageTk.PhotoImage(img)

canvas.create_image(100, 100, image=image_logo)
canvas.image = image_logo  # keep a reference to the image so it isn't garbage-collected
canvas.create_rectangle(0,0,199,199)
canvas.grid(row=0, column=1)

web_label = Label(text='Website: ')
web_label.grid(row=1,column=0, pady=5)

web_input = Entry(width=40)
web_input.grid(row=1, column=1, columnspan=2, pady=5)

email_label = Label(text='Email/Username: ')
email_label.grid(row=2,column=0)

email_input = Entry(width=40)
email_input.grid(row=2, column=1, columnspan=2)

pass_label = Label(text='Password: ')
pass_label.grid(row=3,column=0)

pass_input = Entry(width=22)
pass_input.grid(row=3, column=1)

pass_button = Button(width=18, text='Generate Password')
pass_button.grid(row=3, column=2)

add_button = Button(width=40, text='Add')
add_button.grid(row=4, column=1, columnspan=2)


















# canvas.bind("<Button-1>", get_coordinates)
root.mainloop()


