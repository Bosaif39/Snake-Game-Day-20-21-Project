# Snake file
from turtle import Turtle

distance = 20
starter = [(0, 0), (20, 0), (40, 0)]
up = 90
down = 270
left = 180
right = 0


class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        for i in starter:
            self.adder(i)

    def move(self):
        for i in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[i - 1].xcor()
            new_y = self.parts[i - 1].ycor()
            self.parts[i].goto(new_x, new_y)
        self.head.forward(distance)

    def up(self):
        if self.head.heading() != down:
           self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
           self.head.setheading(down)

    def right(self):
        if self.head.heading() != left:
           self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
           self.head.setheading(left)

    def adder(self, i):
        p1 = Turtle("square")
        p1.color("white")
        p1.penup()
        p1.goto(i)
        self.parts.append(p1)

    def big(self):
        self.adder(self.parts[-1].position())
