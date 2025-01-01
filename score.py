from turtle import Turtle

class Score(Turtle):

    def __init__(self, player):

        super().__init__()

        self.score = 0
        self.player = player

        self.speed(0)
        self.hideturtle()
        self.penup()
        self.color('#ADC178')

        if self.player == 'p1': self.goto(-50, 250)
        elif self.player == 'p2': self.goto(50, 250)

        self.write(f'{self.score}', align= 'Center', font= ['Arial', 20, 'bold'])

    def update(self):
            
        self.score += 1
        self.clear()
        self.write(f'{self.score}', align= 'Center', font= ['Arial', 20, 'bold'])

            

