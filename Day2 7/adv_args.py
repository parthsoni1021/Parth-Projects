def my_func(a,b=4,c=9):      # b,c are by default set to some value. These now became optional
    print(a,b,c)
    return a+b+c

my_func(c=3,a=1,b=5)
my_func(4, b=5)         # my_func(b=5) will give error. First argument will be same as that in function, or else positional


def add1(n1,n2):
    return n1+n2   

# add1(4,6,8,2,5)  # This gives error

def add(*args):            # Unlimited positional arguments - Positional, because the tuple are sequential, where position matters
    sum = 0
    for n in args:
        sum += n
    print(sum, type(args))
    print(args[0])              # referred an argument by position
    return sum

add(4,6,8,2,5)

# How to refer an argument by name, rather than position

def calculate(n, **kwargs):            # Unlimited keyword arguments
    print(kwargs, type(kwargs))
    for (key,value) in kwargs.items():
        print(key)
        print(value)
    print(kwargs['add'])       # referred an argument by position

    n += kwargs.get('add')
    n *= kwargs['multiply']
    print(n)
    
calculate(2, add=3, multiply=6)

# tkinter was ported from Tk, which had a very different syntax from python. 
# Developers turned all the featured from Tk to kwargs

class Car:
    def __init__(self, **kw):
        self.make = kw['make']
        self.model = kw.get('model')    # returns None if the argument isn't there, so doesn't throw error
        self.color = 'Blue'
        self.seats = kw.get('seats')
        
my_car = Car(make='Nissan')   # make is necessary to by inputted. Else it will give error
print(my_car)
print(my_car.make)
print(my_car.model)
print(my_car.color)















