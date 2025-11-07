from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"

#------------------------------------------------------------------------------------

with open("Day31/data/french_words.csv",encoding='utf-8') as french_csv:
    df = pandas.read_csv(french_csv)
    
    # print(df.head())
    

fr_en_dict = df.to_dict(orient='records')  #[{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'}]
random_word = {}

def choose_random_word():
    global random_word
    random_word = random.choice(fr_en_dict)
    french_word = random_word.get('French')
    canvas.itemconfig(canvas_word, text=french_word)
    canvas.itemconfig(canvas_title, text='French')


def flip_card():
    canvas.itemconfig(canvas_title, text='English')
    canvas.itemconfig(canvas_word, text = random_word.get('English')) 

# --------------------------------UI Setup -------------------------------------
window = Tk()
window.minsize()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
   

window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
back_image = PhotoImage(file=r"Day31\images\card_back.png")
front_image = PhotoImage(file=r'Day31\images\card_front.png')
canvas_image = canvas.create_image(400, 263, image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_title = canvas.create_text(400,150, text='title', font=('Arial', 40, 'italic'))
canvas_word = canvas.create_text(400,263, text=random_word.get('French'), font=('Arial', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file=r'Day31\images\right.png')
right_button = Button(image = right_image, highlightthickness=0, command=choose_random_word)
right_button.grid(row=1, column=1) 

wrong_image = PhotoImage(file=r'Day31\images\wrong.png')
wrong_button = Button(image = wrong_image, highlightthickness=0, command=choose_random_word)
wrong_button.grid(row=1, column=0) 

window.mainloop()