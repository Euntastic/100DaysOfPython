from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.move_speed = 0.05
        self.x_move = 10
        self.y_move = 10

        self.color('white')
        self.penup()
        self.shape('square')
        self.shapesize(0.7, 0.7)

        self.reset_self()


    def reset_self(self):
        self.goto(0, 0)
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9