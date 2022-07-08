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

cars = CarManager()
background = BackGround()
player_turtle = Player()
scoreboard = Scoreboard()

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
    if len(cars.all_lanes) < 15:
        cars.create_cars()
    if len(cars.all_lanes) > 1:
        cars.populate_lane()
    cars.move_cars()

    if player_turtle.ycor() >= 180:
        player_turtle.has_crossed()
        scoreboard.player_score += 1
        scoreboard.update_score()
    elif scoreboard.player_lives == -1:
        scoreboard.game_over()
        game_is_on = False
    for car in cars.all_lanes:
        if player_turtle.distance(car) < 28:
            player_turtle.hit_by_car()
            scoreboard.player_lives -= 1
            scoreboard.update_score()
    loop_count += 1


screen.exitonclick()