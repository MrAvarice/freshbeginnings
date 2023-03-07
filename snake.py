import turtle
from turtle import Turtle

starting_p = [(0, 0), (-20, 0), (-40, 0)]
segments = []
MOVE = 15
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
x = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_p:
            self.add(position)

    def extend(self):
        self.add(self.segments[-1].position())

    def add(self, position):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(position)

        self.segments.append(tim)

    def movement(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()

            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
