from turtle import Turtle

STARTING_POSITION = (0, -220)
MOVE_DISTANCE = 40
FINISH_LINE_Y = 180

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.x_coord = 0
        self.y_coord = -220
        self.hixbox = MOVE_DISTANCE / 2
        self.lives = 6
        self.penup()
        self.shape('turtle')
        self.turtlesize(outline= 0.4)
        self.color('black', 'sea green')
        self.reset_player()
    
    def reset_player(self):
        self.seth(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.goto(self.x_coord, self.y_coord)

    def move_up(self):
        self.seth(90)
        if self.y_coord < 180:
            self.y_coord += MOVE_DISTANCE 
            self.move()

    def move_down(self):
        self.seth(270)
        if self.y_coord > -220:
            self.y_coord -= MOVE_DISTANCE
            self.move()

    def move_left(self):
        self.seth(180)
        if self.x_coord > -180:
            self.x_coord -= MOVE_DISTANCE
            self.move()

    def move_right(self):
        self.seth(0)
        if self.x_coord < 180:
            self.x_coord += MOVE_DISTANCE
            self.move()