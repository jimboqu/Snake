from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.color("white")
        self.display_score()
        self.hideturtle()

    def display_score(self):
        self.write(f"Score: {self.score} ", align="center", font=('Arial', 12, 'bold'))

    def score_update(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=('Arial', 12, 'bold'))

