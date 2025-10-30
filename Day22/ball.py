from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
    def init_ball(self):
        x_pos = self.xcor()
        y_pos = self.ycor()
        x_pos += self.x_move
        y_pos += self.y_move
        self.goto(x_pos, y_pos)
        
            
    def bounce_y(self):
        self.y_move *= -1 
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.97
        
    def did_collide(self):
        if self.ycor() > 285 or self.ycor() < -285:
            return True    
    
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
        