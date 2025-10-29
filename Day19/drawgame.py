# Python higher order Functions and Event Listeners

from turtle import Turtle, Screen

# Objects creation
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)
    
def turn_right():
    tim.right(10)
    
def turn_left():
    tim.left(10)
    
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()    
    
screen.listen()
screen.onkey(key='w', fun=move_forward) #IMP: When we pass function as input, we need to see if to add ()
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(clear, 'c')

# onkey is an event handler, and takes function with no argument given

screen.exitonclick()

"""
*********************************
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

def calculator(n1,n2,func):
    return func(n1,n2)

result = calculator(7,3,multiply)
--> Calculator is a higher order function.
************************************
"""





