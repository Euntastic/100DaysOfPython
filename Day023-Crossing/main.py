import time
from turtle import Screen
from player import Player
from background import BackGround
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=480, height=640)
screen.tracer(0)
player_turtle = Player()
background = BackGround()
cars = CarManager()

screen.listen()
screen.onkeypress(fun=player_turtle.move_up, key='Up')
screen.onkeypress(fun=player_turtle.move_down, key='Down')
screen.onkeypress(fun=player_turtle.move_left, key='Left')
screen.onkeypress(fun=player_turtle.move_right, key='Right')

loop_count = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    if len(cars.all_lanes) > 1:
        cars.populate_lane()
    cars.move_cars()

    loop_count += 1


screen.exitonclick()