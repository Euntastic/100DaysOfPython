from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        # 0, 20, 40, 480(240)/640(320)=16
        self.respawn()

    def respawn(self):
        random_x = random.randint(-10, 10) * 20
        random_y = random.randint(-14, 13) * 20
        self.goto(random_x, random_y)