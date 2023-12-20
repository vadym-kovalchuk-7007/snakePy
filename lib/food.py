from turtle import Turtle
import random


def get_new_pos() -> int:
    from_: int = -200
    to_: int = 200

    return random.randint(from_, to_)


class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(get_new_pos(), get_new_pos())
