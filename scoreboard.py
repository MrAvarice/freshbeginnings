import turtle
from turtle import Turtle
import snake

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.update()

    def update(self):
        self.write(f"Score: {self.score} ", False, align="center", font=("Arial", 14))

    def gameover(self):
        self.goto(0, 0)
        self.write(f"Game Over score: {self.score} ", False, align="center", font=("Arial", 14))

    def increase(self):
        self.score += 1
        self.clear()
        self.update()