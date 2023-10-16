from turtle import Turtle,Screen
from interface import Interface
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
ball = Ball()
face1 = Interface("left")
face2 = Interface("right")
face3 = Interface("board")

paddle = Paddle()
screen.listen()
screen.onkey(fun=paddle.up_l,key="w")
screen.onkey(fun=paddle.down_l,key="s")
screen.onkey(fun=paddle.up_r,key="Up")
screen.onkey(fun=paddle.down_r,key="Down")
# screen.onkey(fun=paddle.up("right"),key="Up")
# screen.onkey(fun=paddle.down("left"),key="Down")
# screen.onkey(fun=paddle.up("right"),key="w")
# screen.onkey(fun=paddle.down("left"),key="s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce1()


    if ball.distance(paddle.paddle[1]) < 50 and ball.xcor() > 320:
        ball.bounce2()
    if ball.xcor() > 380:
        ball.reset()
        face2.update_score()
    if ball.xcor() < -380:
        ball.reset()
        face1.update_score()
    if ball.distance(paddle.paddle[0]) < 50 and ball.xcor() < -320:
        ball.bounce2()


screen.exitonclick()