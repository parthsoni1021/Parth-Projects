# Creating your own class - Our own Blueprint to create our own objects

class User:            # a website's user let say. Written in PascalCase. camelCase is similar to PascalCase except it's first letter is small
    pass       

# now we've wrote the class declaration

# user_1 = User()              # object generally written in snake_case
# user_1.id = '001'
# user_1.username = 'parth'    # attribute assignment ( basically variable for a class )

# print(user_1.id)

# user_2 = User()
# user_2.id = '002'
# user_2.username = 'arsh'

# Now to avoid this repetition of making attributes for every object, we use constructors (initialization)

class Car:
    def __init__(self,seat):
        print('This will be called each time when a object is created')
        self.seat = seat

car_1 = Car(4)    # Output: "This will be called each time when a object is created"
car_1.seat = 5
print(car_1.seat)

# Now how to set values of attributes 
class Jeep:
    def __init__(self, seats):
        self.seats = seats                       # this self.seat is equivalent to user_2.id

jeep_1 = Jeep(6)

print(jeep_1.seats)

class EliteHotel:
    def __init__(self, name, location):
        self.name = name
        self.city = location
        self.type = 'elite'       #This does not make sense to write again and again, so we have set a constant value

hotel_1 = EliteHotel('Taj', 'Mumbai')

print(hotel_1)
print(hotel_1.city)
print(hotel_1.name)
print(hotel_1.type)

# hotel_2 = EliteHotel('Hyatt')   # This will give error as we didn't initialize the city attribute