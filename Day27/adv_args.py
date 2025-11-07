# Advanced arguments and default values
def my_func(a=1, b=2, c=3):
    print(a, b, c)
    return a+b+c

print(my_func(5))  #note that is returns 10, not 6 or throw error


def add1(*args):                 # * operator is used to provide any number of positional 
                                    # arguments as tuple to a function
    print((args), type(args))   # this means, the add function can accept any number of arguments
    sum = 0
    for n in args:
        sum += n
    return sum

print(add1(1,4,7,2,8))

def add(*args):
    print(args[0])    #access tuple index

print(add(32,6,8,3,6,5,1))

# How to refer arguments by name rather than by index

# **kwargs - allow us to work with arbitrary (unlimited) number of keyword arguments

"""def calculate(**kwargs):
    print(kwargs, type(kwargs))                 # a box standard dictionary
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(kwargs['add'])"""

## Datatype of args is tuple, while that of kwargs is dict
def all_aboard(a, *args, **kwargs):
    print(a, args, kwargs)
all_aboard(4,7,3,0,x=10,y=20)


def calculate(n,**kwargs):
    print(kwargs)                 # a box standard dictionary
    n += kwargs['add']
    n *= kwargs['multiply'] 
    print(n)

calculate(5, add=3, multiply=5)
# This gives us a more flexible way of working with arguments, and a way of naming the values we are passing to the function

class Car:
    def __init__(self, **kw):
        self.make = kw['make']         #optional keyword Arguments make and model
        self.model = kw['model']

my_car = Car(make="Nissan", model='GT-R')
print(my_car.model, my_car.make)

# Using get method instead of square brackets to access dictionary values

class Car2:
    def __init__(self, **kw):
        self.make = kw.get('make')         #optional keyword Arguments make and model
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seats = kw.get('seats')

# this is similar to how tkinter module is written from tk
my_car = Car2(make="Nissan", model='GT-R')
print(my_car.model, my_car.make, my_car.color, my_car.seats)
