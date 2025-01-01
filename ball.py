from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        
        super().__init__('circle')
        
        # velocity of x and y values
        self.dx = 6
        self.dy = 6

        self.color('white')
        self.shapesize(stretch_wid=.75, stretch_len=.75)
        self.speed(0)

    def move(self):

        self.penup()
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)
        self.speed(0)