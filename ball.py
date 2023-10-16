from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(self.xcor() +self.x_move  , self.ycor()+self.y_move)

    def bounce1(self):
        self.y_move *= -1

    def bounce2(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    def reset(self):
        self.x_move *= -1
        self.y_move = 10
        self.goto(0, 0 )
        self.move_speed = 0.1

