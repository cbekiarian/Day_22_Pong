from turtle import Turtle,Screen

ALIGNMENT = "Center"
FONT = ("Arial",24,"normal")


class Interface(Turtle):
    def __init__(self, item):
        """Poggers"""
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.score = 0
        self.penup()
        self.pencolor("white")
        if item == "left":
            self.goto(-50, 240)
            self.update_score()
        elif item == "right":
            self.goto(50, 240)
            self.update_score()
        elif item == "board":
            self.set_board()
        else:
            print("something is wrong")

    def update_score(self):
            self.clear()
            self.write(arg = self.score,align= ALIGNMENT,font=FONT)
            self.score += 1



    def set_board(self):
        self.goto(0,290 )
        self.pensize(3)
        self.setheading(270)
        for i in range(300,-300,-20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)