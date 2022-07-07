from turtle import Turtle

STARTING_POSITION = (240, -220)
MOVE_DISTANCE = 40
FINISH_LINE_Y = 180
WIDTH, HEIGHT = 480, 640

class BackGround(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.seth(0)
        self.draw_level()
    
    def draw_line(self, x, y):
        self.width(MOVE_DISTANCE)
        self.goto(x * -1, y)
        self.pendown()
        self.goto(x, y)
        self.penup()

    def draw_dashes(self):
        self.pendown()
        self.forward(7)
        self.penup()
        self.forward(8)

    def draw_separator(self, x, y):
        self.width(1)
        self.goto(x * -1, y)
        for i in range(0, int((WIDTH / 15))):
            self.draw_dashes()


    def draw_level(self):
        for lane in range(0, 11):
            new_y = STARTING_POSITION[1] + (lane * 40)
            if lane in range(1, 5) or lane in range(6, 10):
                self.color('grey20')
            else:
                self.color('dark green')
            self.draw_line(x= STARTING_POSITION[0], y= new_y)
            if lane in range(1, 4) or lane in range(6, 9):
                new_y += MOVE_DISTANCE / 2
                self.color('yellow')
                self.draw_separator(x= STARTING_POSITION[0], y= new_y)