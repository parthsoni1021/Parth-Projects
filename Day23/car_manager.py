COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5  
MOVE_INCREMENT = 5

from turtle import Turtle
import random

class CarManager:                        # This need not inherit from Turtle class
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def make_car(self):
        random_int = random.randint(1,6)
        if random_int == 1:
            new_car = Turtle()  
            new_car.shape('square')   # Mutating  and non-mutating functions/methods
            new_car.shapesize(stretch_len=2, stretch_wid=1)    #40*20 object
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-250,250)
            new_car.goto(300, random_y )
            self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    