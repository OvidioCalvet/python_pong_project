from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor('#373D20')

player_one_score = Score(player='p1')
player_two_score = Score(player='p2')
game_narrator = Score(player='NA')

player_one = Paddle(position='left')
player_two = Paddle(position='right')

game_ball = Ball()


game_is_not_over = True

while game_is_not_over:

    round_is_not_over = True

    while round_is_not_over:

        screen.listen()
        # Paddle Restrictions
        if player_one.ycor() + 40 == 300: screen.onkeypress(player_one.stop, 'w')
        else: screen.onkeypress(player_one.up, 'w')

        if player_one.ycor() - 40 == -300: screen.onkeypress(player_one.stop, 's')
        else: screen.onkeypress(player_one.down, 's')

        if player_two.ycor() + 40 == 300: screen.onkeypress(player_two.stop, 'i')
        else: screen.onkeypress(player_two.up, 'i')

        if player_two.ycor() - 40 == -300: screen.onkeypress(player_two.stop, 'k')
        else: screen.onkeypress(player_two.down, 'k')

        game_ball.move()

        # Wall detection & bounce
        if game_ball.ycor() > 290: game_ball.dy *= -1

        elif game_ball.ycor() < -290: game_ball.dy *= -1

        elif game_ball.xcor() > 435: 
            
            round_is_not_over = False
            player_one_score.update()

        elif game_ball.xcor() < -435: 
            
            round_is_not_over = False
            player_two_score.update()
            

        # Paddle detection & bounce
        if game_ball.xcor() > player_two.xcor() - 10: 

            if game_ball.ycor() < player_two.ycor() + 60 and game_ball.ycor() > player_two.ycor() - 60:

                game_ball.dx *= -1

        elif game_ball.xcor() < player_one.xcor() + 10:

            if game_ball.ycor() < player_one.ycor() + 60 and game_ball.ycor() > player_one.ycor() - 60:

                game_ball.dx *= -1

    if player_one_score.score == 11:
        
        game_is_not_over = False
        game_ball.hideturtle()
        game_narrator.print_winner(winner= 'Player 1')

    elif player_two_score.score == 11:

        game_is_not_over = False
        game_ball.hideturtle()
        game_narrator.print_winner(winner= 'Player 2')
        
    else: game_ball.goto(0,0)

screen.exitonclick()

    
