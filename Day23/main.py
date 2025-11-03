import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

timmy = Player()
screen.listen() 
screen.onkey(fun=timmy.go_up, key='Up')   #func will be triggered only when the up key is pressed

car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.make_car()
    car_manager.move_cars()
    
    # Detect collison with cars
    for car in car_manager.all_cars:
        if car.distance(timmy) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect a successful crossing
    if timmy.is_at_finish_line():
        timmy.goto_start()
        car_manager.level_up()     # Increase the speed of cars
        scoreboard.increase_level()
        scoreboard.update_scoreboard()

screen.exitonclick()
