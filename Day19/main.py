# Object State and Instances - Turtle racing game
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400) #In such cases, use keyword arguments
user_bet = screen.textinput(title = 'Make your bet', prompt = 'Which turtle will win the race? Enter a color: ')

# Create Instances of Turtle class. Each object can have different states
colors = ['red','yellow','green','blue','purple','orange']
y_pos = [-70,-40,-10,20,50,80]
all_turtles = []
for turtle_index in range(0,6):
    new_turtle = Turtle(shape = 'turtle')
    new_turtle.speed('slowest')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])  #turtle is 40*40 object
    all_turtles.append(new_turtle)

is_race_on = False
#We can just use speed function and randomly allot to each, but we'll make it unpredictable

if user_bet:
    is_race_on = True
    
while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print("You've won!")
            else:
                print('You\'ve lost')
                
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()