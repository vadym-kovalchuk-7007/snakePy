from turtle import Turtle

MOVE_DISTANCE: int = 20
STARTING_POSITIONS: list(tuple[int, int]) = [(0, 0), (-20, 0), (-40, 0)]
RIGHT: int = 0
UP: int = 90
LEFT: int = 180
DOWN: int = 270
MEASURES = [-280, 280]


def create_turtle_segment() -> Turtle:
    segment: Turtle = Turtle("square")
    segment.pu()
    segment.color("white")

    return segment


class Snake:
    snake: list[Turtle] = []

    def __init__(self):
        self._create_snake()
        self.head = self.snake[0]
        self.head.color("red")  # dev

    """
        Creates a snake by adding turtle segments to the snake list.

        Parameters:
        - self: The SnakeGame object.

        Returns:
        - None

        Description:
        - This function creates a snake by adding three turtle segments to the snake list.
        - Each segment is positioned at a specific coordinate on the screen.
        - The turtle segment is then made visible and added to the snake list.
        - The color of the first segment is set to red for development purposes.
        """

    def _create_snake(self) -> None:
        for pos in STARTING_POSITIONS:
            segment: Turtle = create_turtle_segment()
            segment.goto(pos)
            segment.st()
            self.snake.append(segment)

    def extend(self) -> None:
        segment: Turtle = create_turtle_segment()
        tail: Turtle = self.snake[-1]
        segment.goto(tail.xcor(), tail.ycor())
        self.snake.append(segment)

    """
        Moves the snake forward by one segment.

        This method is responsible for moving the snake forward by one segment. It updates the position of each segment
        of the snake by copying the position of the previous segment. The head of the snake moves forward by a fixed
        distance defined by the constant MOVE_DISTANCE.

        Parameters:
        - self: The Snake object.

        Returns:
        - None

        Example:
        snake = Snake()
        snake.move()
        """

    def move(self) -> None:
        for i in range(len(self.snake) - 1, 0, -1):
            segment_x_pos = self.snake[i - 1].xcor()
            segment_y_pos = self.snake[i - 1].ycor()
            self.snake[i].goto(segment_x_pos, segment_y_pos)
        self.head.forward(MOVE_DISTANCE)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def check_food_dist(self, food) -> bool:
        return self.head.distance(food) <= 15

    def check_collision(self) -> bool:
        for segment in self.snake:
            if segment != self.head:
                print(f"Collision {self.head.distance(segment) < 10}")
                return self.head.distance(segment) < 10

    def check_wall(self) -> None:
        x_pos = self.head.xcor()
        y_pos = self.head.ycor()
        is_out_x = self._check_measures(x_pos)
        is_out_y = self._check_measures(y_pos)
        if is_out_x:
            print(f"isOutx {x_pos}")
            self.head.goto(self._get_new_position(pos=x_pos), y_pos)
        if is_out_y:
            print(f"isOut Y {y_pos}")
            self.head.goto(x_pos, self._get_new_position(pos=y_pos))

    @staticmethod
    def _check_measures(pos: float, padding: int = 0) -> bool:
        return pos < MEASURES[0] - padding or pos > MEASURES[1] + padding

    def _get_new_position(self, pos: float) -> float:
        if self._check_measures(pos):
            return pos * -1
        else:
            return pos
