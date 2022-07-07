from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(640, 480)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)

ball = Ball()
l_paddle = Paddle( x = -300 )
r_paddle = Paddle( x =  300 )
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(fun=l_paddle.move_up, key='Up')
screen.onkeypress(fun=l_paddle.move_down, key='Down')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 200 or ball.ycor() < -200:
        ball.y_bounce()
    
    # Collision Testers Start
    if ball.xcor() > 300 or ball.xcor() < -300:
        scoreboard.update_screen(x= int(ball.xcor()))
        if scoreboard.p1_score == 9 or scoreboard.p2_score == 9:
            scoreboard.win_screen()
            game_is_on = False
        ball.reset_self()
        l_paddle.reset_self()
        r_paddle.reset_self()


    r_paddle.goto(300, ball.ycor())
    # l_paddle.goto(-300, ball.ycor())
    # Collision Testers End

    # Detect collision
    if ball.distance(r_paddle) < r_paddle.hitbox and ball.xcor() + 5 > 290:
        ball.x_bounce()

    if ball.distance(l_paddle) < l_paddle.hitbox and ball.xcor() + 5 < -275:
        ball.x_bounce()

screen.exitonclick()