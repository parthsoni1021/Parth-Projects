"""# Object oriented programming systems

# procedural -> Functional -> Object oriented
# List, string etc. all were classes

class Student:
    college_name = "ABC College"   #class attribute. Stored only once in memory, as not defined with self

#parameterized constructor
    def __init__(self, fullname, marks):                 # always takes the self parameter. Refers to the object itself
        print(self)                               # self is an alias. Can write anything else
        self.name = fullname
        self.marks = marks
        print('adding new student in database..')

    def welcome(self):   #method always takes self argument
        print("Welcome student", self.name)

    @staticmethod   # Don't use a self parameter, and works at class level
    def hello():
        print("Hello")

    def get_marks(self):
        return self.marks
    
# create object (instances of class)
s1 = Student('karan', 95.1)
print(s1)
print(s1.name)

s2 = Student('arjun', 92.4)
print(s2.marks, s2.name)
print(s2.college_name)
print(Student.college_name)  #directly call class.attr only for class attributes

print(s1.welcome())         #prints 'Welcome student' and 'None'
s1.hello()             # Had it not been a static method, it would have showed error that hello takes 0 positional 
# argument, but one (self) was given.


class Car:
    color = "Blue"
    brand = 'Mercedes'
# We didn't write an init function, so python automatically created it at backend.
    def __init__(self):          # default constructor           
        pass

car1 = Car()   #this () after Car is to invoke constructor only
print(car1.color)
print(car1.brand)

car1.color = 'Black'  #change attribute value directly if needed
print(car1.color)
# Constructor - __init__ function
# Invoked (executed) during object creation. It is a reference to the current instance of the class and is used 
# to access variables that belongs to the class (attributes)


# Methods 
# Static Methods


# Pillars of OOP: Abstraction, Encapsulation, Inheritance, and Polymorphism
# Abstraction: Hiding the implementation details of a class, and showing the essential features to user.
# Encapsulation: Wrapping data and related functions into a single unit (object).



# Quesition:
# Create account class with 2 attributes - balance and account number
# Create methods for debit, credit and printing the balance

class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self. acc_no = acc_no

    def debit(self, amount):
        self.balance -= amount
        statement = f"Amount {amount} has been deducted from your account. Current balance = {self.get_balance()}"
        print(statement)
        return statement
    
    def credit(self, amount):
        self.balance += amount
        statement = f"Amount {amount} has been added from your account. Current balance = {self.get_balance()}"
        print(statement)
        return statement

    def get_balance(self):
        return self.balance 

acc1 = Account(10000, 123455)
print(acc1.get_balance())
acc1.credit(2500)   



class Cars():
    def __init__(self):
        self.acc = False
        self.brake = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print('Car Started..')

car1 = Cars()
car1.start()

# del keyword - used to delete object properties or object itself, or methods from a class.

class Students:
    def greet(self):
        print("Hello!")

s = Students()
del Students.greet  # Remove method from this instance
# s.greet()  # Raises AttributeError

# Private(like) attributes and methods

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass   

    def reset_pass(self):
        print(self.__acc_pass)
        return None

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()

acc1 = Account('12345', 'abcde')
print(acc1.acc_no)
# print(acc1.__acc_pass) gives error
acc1.reset_pass()    # This though won't give an error as this attribute is used within class
# acc1._hello()   gives error
acc1.welcome()

# Inheritance
# Single, Multi-Level and Multiple Inheritance

class Jeep:           # Parent class
    @staticmethod
    def start():
        print('Car started')

    @staticmethod
    def stop():
        print("Car Stopped")

class ToyotaCar(Jeep): # Child class``
    def __init__(self, brand):
        self.brand = brand

    def greet(self, name):
        print('Welcome to Toyota child Class', name)

car1 = ToyotaCar('Fortuner')
car2 = ToyotaCar("Prius")

print(car1.brand)
car1.start()

class Fortuner(ToyotaCar):
    def __init__(self, type, id, brand):
        self.type = type
        self.id = id
        super().__init__(brand)      # Super method - Used to access method of the parent class
        
car1 = Fortuner('Diesel', '142','Fortuner')
car1.start()
print(car1.brand)     

car1.greet('parth')

# Multiple Inheritance - Can be inherited from multiple base classes
class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varA)


# Class method - Bound to the class and receives the class as an implicit first argument
# Static methods can't access or modify class state and geneally for utility 

class Person():
    name = 'anonymous'

    def change_name(self, name):
        self.name = name

p1 = Person()
p1.change_name("parth")
print(p1.name)

print(Person.name)
# This change_name wasn't able to change the class attribute.
# A new name attribute inside object was made

class Person2():
    name = 'anonymous'

    def change_name(self, name):
        Person2.name = name

p2 = Person2()
p2.change_name("parth")
print(p2.name)
print(Person2.name)

# OR
class Person3():
    name = 'anonymous'

    def change_name(self, name):
        self.__class__.name = name

p3 = Person3()
p3.change_name("parth")
print(p3.name)
print(Person3.name)

# OR - Use class method, where first argument is class, not self

class Person4():
    name = 'anonymous'

    @classmethod
    def change_name(cls, name):
        cls.name = name

p4 = Person4()
print(p4.name)
p4.change_name("parth")
print(p4.name)

# Static methods (do not access attributes of class or object), class methods(takes class implicitly), instance methods(takes self implicitly)
# Property decorator

class Student4():
    def __init__(self, phy,che,math):
        self.phy = phy
        self.chem = che
        self.math = math
        # self.percentage = str((self.phy+self.chem+self.math)/3)+("%")

    @property
    def percentage(self):  #
        return str((self.phy+self.chem+self.math)/3)+("%")


stu1 = Student4(79,85,91)
print(stu1.percentage)

stu1.phy = 86
print(stu1.phy)
print(stu1.percentage)   #This won't change if defined with self

stu1.phy = 86
print(stu1.phy)
stu1.percentage
print(stu1.percentage)

#Polymorphism
"""

# Function flatten_list(lst) to convert a nested list like [1, [2, 3], [4, [5,6]]] → [1,2,3,4,5,6].

def flatten_list(list):
    flat_list = []
    for i in list:
        if type(i) in (str, bool, int, float):
            flat_list.append(i)
            


print(flatten_list([1, [2, 3], [4, [5,6]], [1, [2, 3], [4, [5,6]]]]))



























