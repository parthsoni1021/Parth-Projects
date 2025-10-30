# We're gonna build a pong game
from turtle import Turtle, Screen 
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

#Create Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Welcome to the pong game")
screen.bgcolor('black')

screen.tracer(0)
# Create and move a right paddle

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

scoreboard = Scoreboard()

game_is_on = True
ball = Ball()

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.init_ball()
    
# Detect collison with wall (top and bottom) and bounce_y
    if ball.did_collide():
        ball.bounce_y()
        
# Detech collison with the paddle
    # if ball.distance(paddle)   won't work
    if (ball.distance(r_paddle) < 53.85 and ball.xcor() > 330) or (ball.distance(l_paddle) < 53.85 and ball.xcor() < -330):
        ball.bounce_x()
        
    # delect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    # detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        






screen.exitonclick()

