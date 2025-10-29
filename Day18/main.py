# I am going 4 days behind. I need to catch up. 
# Maybe a little sleep, some 1-2 all nighters, and I know I'll do it. IIT exams mode needs to come back.  

# import turtle
# tim = turtle.Turtle()          # This is tedious, but expressive

# from module import class

# import Turtle as t          #alias
from turtle import Turtle as t, Screen
import random

tim = t()

tim.shape("turtle")
tim.color('red')

# for i in range(4):
#     tim.forward(100)
#     tim.right(90) 

import heroes
print(heroes.gen())

# Drawing a dashed line
# for i in range(50):
#     tim.forward(5)
#     if i%2 != 0:
#         tim.pendown()
#     else:
#         tim.penup()
        
        
# drawing a polygon over another, starting from triangle
colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'orange', 'purple', 'violet', 'maroon', 'navy', 'skyblue', 'turquoise', 'lime', 'darkgreen', 'chocolate', 'brown', 'black', 'gray', 'white', 'lightgreen', 'lightsalmon']
side_length = 50
n = 11

# for i in range(3,n+1):
#     side_angle = 360/i
#     tim.color(random.choice(colors))
#     for j in range(i):
#         tim.forward(side_length)    
#         tim.left(side_angle)
        
#better, instead of making nested loop like this, we make a function. 
# def draw_shape(i):
#     side_angle = 360/i
#     tim.color(random.choice(colors))
#     for j in range(i):
#         tim.forward(side_length)    
#         tim.left(side_angle)
    
# for k in range(3,n+1):
#     draw_shape(k)

# Create a random walk
# directions = ['left', 'right', 'forward']
# tim.pensize(3)
# tim.speed('fast')
# last_dir = ""
# for i in range(391):
#     dir = last_dir
#     while dir == last_dir:
#         dir = random.choice(directions)
#     last_dir = dir
        
#     tim.color(random.choice(colors))
    
#     if dir == 'left':
#         tim.left(90)
#         tim.forward(20)
#     elif dir == 'right':
#         tim.right(90)
#         tim.forward(20)
#     else:
#         tim.forward(20)    

# alternatively, use a direction list of angles (*90), then use setheading method



def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    random_col = (r,g,b)
    return random_col
    
def draw_circle(angle):
    tim.pensize(1)
    tim.speed('fastest')
    for i in range(angle):
        tim.color(random_color())
        tim.right(i)
        tim.circle(50)
        
draw_circle(360)












screen = t.Screen()
screen.exitonclick()