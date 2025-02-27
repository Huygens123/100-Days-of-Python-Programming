from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 1
        self.score_loc()

    def score_loc(self):
        self.clear()
        self.goto(-220, 255)
        self.write(f"Level: {self.score}", align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.score_loc()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align='center', font=FONT)

