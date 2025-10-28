#!C:\Users\HD176PR\AppData\Local\anaconda3\python.exe

# Earlier we did procedural programming.  # Fortran, Cobol like languages relied on that
# But this makes the program very complex in relationships, when the problem goes little complex.

# Object oriented paradigmn - mapped properly, and reusable for some other type of code

# Turtle Graphics Module (Library) - A blueprint someone else has already created. We will construct objects from this.
# docs.python.org/3/library/turtle.html 
"""
import turtle

#make an object from class turtle declared inside turtle module

timmy = turtle.Turtle()          # () initialize/construct the object timmy

#OR
# from turtle import Turtle
# timmy = Turtle()

print(timmy)       # <turtle.Turtle object at 0x000001B0B0655C10>
timmy.shape("turtle")
timmy.color('brown1', 'blue')
timmy.forward(100)

from turtle import Screen
my_screen = Screen()               # my_screen object
print(my_screen.canvheight)         # canvheight attribute 
my_screen.exitonclick()             #exitonclick method
"""
# Module is basically another file we make (or import from someone else's)
# Package of Code - A bunch of lots of code other people have written - search on PyPI - Python package index 
# bunch of software developed by python developers community - Can be installed using pip install

from prettytable import PrettyTable
table = PrettyTable()

# print(table)
table.add_column('Pokemon_name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['electric', 'water', 'fire'])

print(table)
print(table.align)
table.align = 'l'
print(table)

class Car():
    pass

my_toyota = Car()
my_fiat = Car()

# my_toyota and my_fiat are the variables and each contains a car object

# ______________________________________________________________________________________________________

from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

menu = Menu()
coffeemaker_instance = CoffeeMaker()        # generally objects are snake_case of the class
moneymachine_instance = MoneyMachine() 

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}")
    
    if choice == 'report':
        coffeemaker_instance.report()
        moneymachine_instance.report()

    elif choice == 'off':
        is_on = False
    
    else:
        drink = menu.find_drink(choice)       
        print(type(drink))             #<class 'menu.MenuItem'>
        if drink is not None:
            if coffeemaker_instance.is_resource_sufficient(drink):
                if moneymachine_instance.make_payment(drink.cost):
                    coffeemaker_instance.make_coffee(drink)


# If the user enters "latte", "espresso", or "cappuccino":
#   drink will be an instance of the MenuItem class.
# If the user enters something else:
#   The method prints "Sorry that item is not available."
#   drink will be None.

# Even though I didn't explicitly create a MenuItem object yourself, the Menu class did when you instantiated it.
        










































