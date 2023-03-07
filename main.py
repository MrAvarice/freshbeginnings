import time
import turtle
from turtle import Screen, Turtle

from scoreboard import Score
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)
x = 0

score = Score()
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.movement()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()
    # detect collision
    if snake.head.xcor() > 299 or snake.head.xcor() < - 299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
        game_is_on = False
        score.gameover()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            score.gameover()


screen.exitonclick()
