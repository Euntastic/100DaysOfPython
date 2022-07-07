from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', '12', 'normal')
DIRECTIONS = [0, 270, 180, 90]
WIDTH, HEIGHT = 420, 580

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.speed("fastest")
        self.update_score()
        self.draw_border()

    def update_score(self):
        self.goto(0, 290)
        self.color("white")
        self.score_text = f"Score: {self.score}"
        self.write(self.score_text, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        self.draw_border()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, \
            font=('Arial', 25, 'bold'))

    def draw_border(self):
        self.goto(-210, 290)
        self.color("grey30")
        self.pendown()
        self.pensize(1)
        for direction in DIRECTIONS:
            self.seth(direction)
            if direction == 0 or direction == 180:
                self.forward(WIDTH)
            else:
                self.forward(HEIGHT)    
        self.penup()