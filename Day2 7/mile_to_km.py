from tkinter import * 
color = '#fdf5e6'

window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20, bg=color)

def converter():
    miles_value = input.get()
    output = float(miles_value)*1.609
    result_label.config(text=output)

miles_label = Label(text='Miles')
miles_label.grid(row=0, column=3)
miles_label.config(bg=color)

km_label = Label(text='Km')
km_label.grid(row=1, column=3)
km_label.config(bg=color)

input = Entry(width=10)
input.grid(row=0, column=1)

is_equal_to_label = Label(text='is equal to')
is_equal_to_label.grid(row=1, column=0)
is_equal_to_label.config(bg=color)

result_label = Label(text = '0')
result_label.grid(row=1, column=1)
result_label.config(bg=color)

calc_button = Button(text='Calculate', command=converter)
calc_button.grid(row=2, column=1)






window.mainloop()