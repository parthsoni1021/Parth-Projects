from tkinter import * 

# PACK -> very broad (wague), 
# PLACE -> very specific (coordinates) 
# GRID -> no. of rows and columns of grid can be defined 

def button_clicked():
    print('I got clicked')
    new_text = input.get()
    my_label.config(text = new_text)
    
window = Tk()
window.title("My first GUI Program")
window.minsize(width=600, height=400)
window.config(padx=100, pady=50)

# Label
my_label = Label(text='I am a Label', font=('Arial',24, 'bold'))  # create a component
my_label.config(text = 'New Text')
my_label.grid(row=0, column=0)                        # How the component will be laid out on the screen before display
   
# Button    
# button = Button(text='Click Here', command=button_clicked)   #sort of event listener
button = Button(text='Click Here', command=button_clicked)
button.grid(column=1, row=1)  
button.config(padx=20, pady=20)        # Padding around window and particualr widget

new_button = Button(text='New button')
new_button.grid(row=0, column=2)

# Entry 
input = Entry(width=20)
print(input.get())
input.grid(column=3, row=2)

# Note: Grid and Pack can't be used in the same program










window.mainloop()  