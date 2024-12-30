from turtle import Turtle

MOVEMENT_INCREMENT = 20

class Paddle(Turtle, ):

    def __init__(self, position):
        
        super().__init__()

        self.hideturtle()
        self.position = position
        self.paddle = self.create_paddle()
        

    def create_paddle(self):

        new_paddle = Turtle('square')
        new_paddle.shapesize(stretch_len=.5, stretch_wid=4)
        new_paddle.color('#ADC178')
        new_paddle.penup()
        new_paddle.speed(0)

        if self.position == 'right': new_paddle.goto(425,0)
        else: new_paddle.goto(-425, 0)

        return new_paddle

    def up(self): self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + MOVEMENT_INCREMENT)

    def down(self): self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - MOVEMENT_INCREMENT)
