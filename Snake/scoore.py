# scoore class
from turtle import Turtle

class Scoore(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.score = 0
        self.update_s()

    def update_s(self):
        self.write(f"Score : {self.score}", align="center", font=("Courier", 24, "normal"))

    def newscoore(self):
        self.score += 1
        self.clear()
        self.update_s()

    def gameover(self):
        if self.score >= 50:
            self.goto(0, 0)
            self.write(f"You win", align="center", font=("Courier", 24, "normal"))
        else:
            self.goto(0, 0)
            self.write(f"GAME OVER", align="center", font=("Courier", 24, "normal"))