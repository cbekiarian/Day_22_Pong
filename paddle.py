from turtle import Screen,Turtle
import random
import time
MOVE_DISTANCE = 20

UP = 90
DOWN =270
RIGHT = 0
LEFT = 180
class Paddle(Turtle):

    def __init__(self):
        self.paddle = []
        self.create_paddle()

    def create_paddle(self):

         for inverse in range(1,-2,-2):

                new_paddle = Turtle("square")
                new_paddle.shapesize(stretch_wid=5,stretch_len=1)
                new_paddle.speed("fastest")
                new_paddle.color("white")
                new_paddle.penup()
                new_paddle.goto(-350* inverse ,0)
                self.paddle.append(new_paddle)

    def up_l (self):
        el = self.paddle[0]
        el.goto(el.xcor(),el.ycor()+20)
    def up_r (self):

        el = self.paddle[1]

        el.goto(el.xcor(),el.ycor()+20)

    def down_l(self):
        el = self.paddle[0]

        el.goto(el.xcor(),el.ycor()-20)


    def down_r(self):
        el = self.paddle[1]

        el.goto(el.xcor(),el.ycor()-20)


