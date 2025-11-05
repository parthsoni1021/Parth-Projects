from tkinter import *

# Pomodoro: 25 work -> 5 break -> 25 work -> 5 break -> 25 work -> 5 break ->25 work -> 20 break

# -------------------------------------- CONSTANTS --------------------------------
PINK = '#e2979c'   #colorhunt.co
RED = '#e7305b'
GREEN = '#9bdeac'
BLUE = '#0000FF'
YELLOW = '#f7f5dd'
FONT_NAME = 'Courier'
WORK_MIN = 25
SHORT_BREAK_MIN = 5 
LONG_BREAK_MIN = 20
reps = 0

# -------------------------------------- TIMER RESET --------------------------------

# -------------------------------------- TIMER MECHANISM ----------------------------

def start_timer():
    global reps
    reps += 1
    
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)
    
    if reps % 8 == 0:
        timer_label.config(text='Long break', font=(FONT_NAME,24,'bold'), bg=YELLOW, fg=RED)
        duration = long_break_sec
    elif reps % 2 == 0:
        timer_label.config(text='Short break', font=(FONT_NAME,24,'bold'), bg=YELLOW, fg=PINK)
        duration = short_break_sec
    else:
        timer_label.config(text='Work, Work !!', font=(FONT_NAME,24,'bold'), bg=YELLOW, fg=BLUE)
        duration = work_sec
        
    countdown(duration)

# -------------------------------------- COUNTDOWN MECHANISM ------------------------
import time
import math

# count = 5             
# while True:
#     time.sleep(1)
#     count -= 1
# Can't use this loop, because GUI programs are event driven. Nothing below this will get executed

def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    
    """ Concept of dynamic typing in python - Python is a strong, and dynamically typed language.
    Perl - weakly typed; Python, JavaScript, Ruby → dynamically typed; Java, C, C++, Rust → statically typed """ 
    
    if count_sec < 10:
        count_sec = f'0{count_sec}'
        
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')   # this is how we change the text in canvas, unlike Label
    if count>0:
        window.after(1000, countdown, count-1)
    else:
        start_timer()
        ticks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            ticks += '✔'
        check_marks.config(text= ticks)
            
        
# -------------------------------------- UI SETUP -----------------------------------
window = Tk()
window.title('Pomodoro')
window.config(padx=30, pady=25, bg=YELLOW)


canvas = Canvas(width=250, height=200, bg=YELLOW, highlightthickness=0)
image_title = PhotoImage(file=r'C:\Users\Parth Soni\OneDrive - IIT Delhi\Documents\Python\100_projects_in_100_days\Day28\tomato.png')
canvas.create_image(125, 79, image=image_title)
timer_text = canvas.create_text(125, 90, text='00:00', fill='white', font=(FONT_NAME, 17, 'bold'))
canvas.grid(row=1,column=1)


timer_label = Label(text='Timer', font=(FONT_NAME,24,'bold'), bg=YELLOW, fg=RED)
timer_label.grid(row=0,column=1)

start_button = Button(text='Start', width=10, command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text='Reset', width=10)
reset_button.grid(row=2,column=2)

check_marks = Label(fg=RED, bg=YELLOW)
check_marks.grid(row=3, column=1)






window.mainloop()   #checks every ms