from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
scoreboard = Scoreboard()

while game_is_on:
    screen.update()
    time.sleep(0.1) 
    snake.move()                                      

    # Detect collision with food - using distance method of turtle library
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.inc_score()
        
    # Detect collision with wall 
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.clear()
        scoreboard.game_over()
        
    # Detect collision with itself
    if snake.self_collision():
        game_is_on = False
        scoreboard.game_over()
    
    
    


    
    


















screen.exitonclick()