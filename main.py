from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor('#373D20')

player_one = Paddle(position='left')
player_two = Paddle(position='right')

game_ball = Ball()

screen.listen()
screen.onkeypress(player_one.up, 'w')
screen.onkeypress(player_one.down, 's')

screen.onkeypress(player_two.up, 'i')
screen.onkeypress(player_two.down, 'k')


game_is_not_over = True

while game_is_not_over:

    round_is_not_over = True

    while round_is_not_over:

        game_ball.move()

        # Wall detection & bounce
        if game_ball.ycor() > 290: game_ball.dy *= -1

        elif game_ball.xcor() > 440: round_is_not_over = False

        elif game_ball.xcor() < -440: game_ball.dx *= -1

        elif game_ball.ycor() < -290: round_is_not_over = False

        # Paddle detection & bounce
        if game_ball.xcor() > player_two.xcor() - 10: 

            if game_ball.ycor() < player_two.ycor() + 60 and game_ball.ycor() > player_two.ycor() - 60:

                game_ball.dx *= -1

        elif game_ball.xcor() < player_one.xcor() + 10:

            if game_ball.ycor() < player_one.ycor() + 60 and game_ball.ycor() > player_one.ycor() - 60:

                game_ball.dx *= -1
    

    
