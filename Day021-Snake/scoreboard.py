from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', '12', 'normal')
WIDTH, HEIGHT = 420, 580

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        
        self.hideturtle()
        with open("hiscore.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.speed("fastest")
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(0, 290)
        self.color("white")
        self.score_text = f"Score: {self.score} High Score: {self.high_score}"
        self.write(self.score_text, align=ALIGNMENT, font=FONT)
        self.draw_border()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("hiscore.txt", mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, \
            font=('Arial', 25, 'bold'))

    def draw_border(self):
        self.goto(-210, 290)
        self.color("grey30")
        self.pendown()
        self.pensize(2)
        self.goto(210, 290)
        self.goto(210, -290)
        self.goto(-210, -290)
        self.goto(-210, 290)   
        self.penup()