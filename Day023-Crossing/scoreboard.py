from asyncore import write
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.hideturtle()
        self.penup()
        self.write_score()

    def write_score(self):
        score_string = f"Score: {self.player_score}"
        self.color('white')
        self.goto(0, 220)
        self.write(score_string, align='center', font=FONT)