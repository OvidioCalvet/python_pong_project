from turtle import Screen
from paddle import Paddle

screen = Screen()
player_one = Paddle()

screen.setup(width=900, height=600)
screen.bgcolor('#373D20')

screen.exitonclick()
