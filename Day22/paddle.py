from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position        #pass a tuple as position
        self.create_paddle()
        
    
    def create_paddle(self):
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)  #by default 20*20 size
        self.goto(self.position)
        
    def go_up(self):
        new_y = self.ycor() + 20
        if new_y < 200:
            self.goto(self.xcor(), new_y)
        else:
            new_y = new_y - 20

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y > -200:
            self.goto(self.xcor(), new_y)
        else:
            new_y = new_y + 20
        
        