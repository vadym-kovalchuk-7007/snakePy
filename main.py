# This is Snake game project

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from turtle import Screen
from lib.snake import Snake
from lib.food import Food
from lib.score import Score
import time

# Screen setup
screen: Screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()

snake: Snake = Snake()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food: Food = Food()
score_board = Score()

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    snake.check_wall()

    if snake.check_food_dist(food):
        food.refresh()
        score_board.add_score()
        snake.extend()

    if snake.check_collision():
        score_board.game_over_msg()
        is_game_on = False

screen.exitonclick()
