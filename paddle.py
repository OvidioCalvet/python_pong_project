from turtle import Turtle

class Paddle(Turtle, ):

    def __init__(self):
        
        super().__init__()

        self.hideturtle()
        self.create_paddle()

        self.position
        self.movement_keys = []

    def create_paddle(self):

        paddle = Turtle('square')
        paddle.shapesize(stretch_len=.5, stretch_wid=4)
        paddle.color('#ADC178')
        paddle.penup()
        paddle.speed(0)

        if self.position == 'right': paddle.goto(425,0)
        else: paddle.goto(-425, 0)
