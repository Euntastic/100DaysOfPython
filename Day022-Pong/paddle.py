from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, player='human'):
        super().__init__()
        self.pong_player = player
        self.hitbox = 35
        self.color('white')
        self.penup()
        self.shape('square')
        self.shapesize(2.5, 0.5, 0)
        self.x_coord = x
        self.reset_self()


    def reset_self(self):
        self.goto(self.x_coord, 0)

    def move_up(self):
        new_y = self.ycor() + 10
        if self.ycor() < 200:
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 10
        if self.ycor() > -200:
            self.goto(self.xcor(), new_y)