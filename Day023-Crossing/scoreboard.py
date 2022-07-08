from asyncore import write
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.player_lives = 6
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_lives(self):
        new_x = -210
        self.seth(90)
        self.shape('turtle')
        self.isvisible()
        self.color('black', 'green')
        self.shapesize(1, 1, 0.4)
        for i in range(self.player_lives):
            self.goto(new_x, -280)
            self.stamp()
            new_x += 20

    def update_score(self):
        self.clear()
        self.update_lives()
        self.hideturtle()
        score_string = f"Score: {self.player_score}"
        self.color('white')
        self.goto(0, 220)
        self.write(score_string, align='center', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=FONT)