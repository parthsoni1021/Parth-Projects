from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self):
        self.window = Tk()                   # creating attributes of the class, not normal variables
        self.window.title('Quizzler')

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='Some Question Text', fill=THEME_COLOR, font=('Arial', 18, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=35)

        true_image = PhotoImage('images/true.png')
        self.true_button = Button(image=true_image, width=100, height=97, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage('images/false.png')
        self.false_button = Button(image=false_image, width=100, height=97, highlightthickness=0)
        self.false_button.grid(row=2, column=1)
        
        self.window.mainloop()
    
    def get_next_question(self):
        pass
    