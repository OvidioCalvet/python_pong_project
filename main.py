from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor('#373D20')

player_one = Paddle(position='right')
player_two = Paddle(position='left')

ball = Ball()

screen.listen()
screen.onkeypress(player_one.up, 'w')
screen.onkeypress(player_one.down, 's')

screen.onkeypress(player_two.up, 'i')
screen.onkeypress(player_two.down, 'k')

game_is_not_over = True

while game_is_not_over:

    pass

screen.exitonclick()
