from turtle import Turtle
SEGMENTS = [
                    [0, 0, 0, 30], [0, 0, 270, 30], [30, 0, 270, 30], 
                    [0, -30, 0, 30], [0, -30, 270, 40], [30, -30, 270, 40],
                    [0, -70, 0, 30]
                        ]
NUMBER_PARTS = [
                    [1, 1, 1, 0, 1, 1, 1], [0, 0, 1, 0, 0, 1, 0], [1, 0, 1, 1, 1, 0, 1], 
                    [1, 0, 1, 1, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0], [1, 1, 0, 1, 0, 1, 1],
                    [1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 0, 1, 1]
                               ]
P1COORD = (-60, 220)
P2COORD = (30, 220)
FONTSTYLE = ('Arial', 50, 'bold')
WIDTH, HEIGHT = 640, 480

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.color('white')
        self.hideturtle()
        self.shape('square')
        self.penup()
        self.draw_middle_line()
        self.update_score()

    def draw_segment(self, x, y, instructions):
        # Instructions List = (x variance, y variance, heading, distance)
        self.goto(x + instructions[0], y + instructions[1])
        self.seth(instructions[2])
        self.pendown()
        self.forward(instructions[3])
        self.penup()

    def draw_number(self, x, y, score):
        self.goto(x, y)
        self.width(7)
        for i, segment in enumerate(NUMBER_PARTS[score]):
            if segment == 1:
                self.draw_segment(x, y, SEGMENTS[i])

    def update_score(self, x= 0):
        if x > 0:
            self.p1_score += 1
        elif x < 0:
            self.p2_score += 1
        self.draw_number(P1COORD[0], P1COORD[1], self.p1_score)
        self.draw_number(P2COORD[0], P2COORD[1], self.p2_score)

    def draw_middle_line(self):
        height_limit = HEIGHT - 20
        self.goto(0, height_limit/2)
        self.shapesize(0.1, 0.4)
        self.seth(270)
        for i in range(1, int(height_limit/17)):
            self.forward(17)
            self.stamp()

    def update_screen(self, x= 0):
        self.clear()
        self.update_score(x)
        self.draw_middle_line()

    def win_screen(self):
        self.goto(0, 0)
        self.color('red')
        winning_player = "Player 1" if self.p1_score == 1 else "Player 2"
        win_text = f"{winning_player} Wins!"
        self.write(win_text, align= 'center', font=FONTSTYLE)
