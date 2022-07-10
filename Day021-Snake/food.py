from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.respawn()

    def respawn(self) -> None:
        random_x = random.randint(-10, 10) * 20
        random_y = random.randint(-14, 13) * 20
        self.goto(random_x, random_y)