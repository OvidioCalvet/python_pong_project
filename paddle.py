from turtle import Turtle

MOVEMENT_INCREMENT = 20

class Paddle(Turtle):

    def __init__(self, position):
        
        super().__init__('square')
        
        self.speed(0)

        #Create Paddle
        self.shapesize(stretch_len=.5, stretch_wid=4)
        self.color('#ADC178')
        self.penup()

        if position == 'right': self.goto(425,0)
        elif position == 'left': self.goto(-425, 0)

    def up(self): self.goto(self.xcor(), self.ycor() + MOVEMENT_INCREMENT)

    def down(self): self.goto(self.xcor(), self.ycor() - MOVEMENT_INCREMENT)

    def stop(self): pass
