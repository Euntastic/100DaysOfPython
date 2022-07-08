import time
import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
LANESCOORD = [-180, -140, -100, -60, 20, 60, 100, 140]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.all_lanes = []

    def move_cars(self):
        for i in range(0, len(self.all_lanes)):
            if self.all_lanes[i].xcor() > -280 or self.all_lanes[i].xcor() < 280:
                self.all_lanes[i].forward(10)

    def set_direction(self, rand_y):
        if rand_y in [-140, -60, 60, 140]:
            return 0, -240
        else:
            return 180, 240

    def populate_lane(self):
        random_y = random.choice(LANESCOORD)
        random_car = random.randint(0, len(self.all_lanes) - 1)
        if self.all_lanes[random_car].xcor() > 280 or self.all_lanes[random_car].xcor() < -280:
            new_heading, x_coord = self.set_direction(random_y)
            self.all_lanes[random_car].seth(new_heading)
            self.all_lanes[random_car].goto(x_coord, random_y)

    def create_cars(self):
        random_chance = random.randint(1, 7)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.choice(LANESCOORD)
            new_heading, x_coord = self.set_direction(random_y)
            new_car.seth(new_heading)
            new_car.goto(x_coord, random_y)
            self.all_lanes.append(new_car)





