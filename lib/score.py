from turtle import Turtle
from typing import Tuple

ALIGN = 'center'
FONT: tuple[str, int, str] = ("Courier", 24, "normal")
COLOR = "grey"


class Score(Turtle):
    score_val: int

    def __init__(self):
        super(Score, self).__init__()
        self.score_val = -1
        self.hideturtle()
        self.color(COLOR)
        self.penup()
        self.goto(0, 265)
        self.add_score()

    def add_score(self) -> None:
        self.score_val += 1
        self.clear()
        self.user_message(f"Score: {self.score_val}")

    def user_message(self, message: str) -> None:
        self.write(message, align=ALIGN, font=FONT)

    def game_over_msg(self) -> None:
        self.goto(0, 0)
        self.user_message("Game is over!")
