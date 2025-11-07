from tkinter import * 

window = Tk()
window.title("My first GUI Program")
window.minsize(width=600, height=400)

# Label
my_label = Label(text='I am a Label', font=('Arial',24, 'bold'))  # create a component
my_label.pack()                        # How the component will be laid out on the screen before display

my_label['text'] = 'New Text'
my_label.config(text= "Another Text")

# Button
def button_clicked():
    print('I got clicked')
    my_label.config(text = 'Button Got Clicked')

def show_text():
    stringoutput = input.get()    # return input as string
    my_label.config(text = stringoutput )
    print(stringoutput)
    
# button = Button(text='Click Here', command=button_clicked)   #sort of event listener
button = Button(text='Click Here', command=show_text)
button.pack()   

# Entry 
input = Entry(width=50)
input.insert(0, string='Some text to begin with')
print(input.get())
input.pack()

#Text
text = Text(height=5,width=27)
text.focus()        #Puts cursor in textbox
text.insert(END, 'Example of Multi-line text entry')  # Add some text to start with
print(text.get('1.0', END))    # get current value in textbox at line1, char 0
text.pack()

# Spinbox
def spinbox_used():
    print(spinbox.get())    # gets the current value in spinbox 
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()  

# Scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Check Button
def checkbutton_used():
    print(checked_state.get())    # print 1 if box is checked, otherwise 0

checked_state = IntVar()    # variable to hold on to checked state, 0 is off, 1 is on
checkbutton = Checkbutton(text='Is On?', variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radio Button           MCQs basically
def radio_used():
    print(radio_state.get())

radio_state = IntVar()   # Variable to hold on to which radio button value is checked
radiobutton1 = Radiobutton(text='Option 1', value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text='Option 2', value=2, variable=radio_state, command=radio_used)

radiobutton1.pack()
radiobutton2.pack()

# Listbox
def listbox_used(event):                             # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ['Apple', 'Banana', 'Guava', 'Orange']

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()








window.mainloop()   