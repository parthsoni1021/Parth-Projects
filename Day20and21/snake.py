from turtle import Turtle
STARTING_POS = [(0,0), (-20,0), (-40,0)] 
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        # Now this code here will determine what should happen when we initialize a new object of Snake class
        self.segments = []  # a new attribute will be created
        self.create_snake()  # a method would be called
        self.head = self.segments[0]  #this need to come after the create_snake(), else error
        
    def create_snake(self):
        for position in STARTING_POS:
            self.add_segment(position)
    
    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.color('blue')
        new_segment.shape('turtle')
        new_segment.penup()
        new_segment.goto(position)         
        self.segments.append(new_segment)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def extend(self):
        self.add_segment(self.segments[-1].position())   #This position is a method
    
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
        # print(seg_num)     # 2 1 2 1 2 1 2 1 
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    



    
    
    
    
    
    
    
    
    
