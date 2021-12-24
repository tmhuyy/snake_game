from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    x = 0

    # create a snake
    def __init__(self):
        self.segments = []
        for _ in range(3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(0 - Snake.x, 0)
            self.segments.append(snake)
            Snake.x += 20
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def increase(self):
        x_cor = self.tail.xcor()
        y_cor = self.tail.ycor()
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(x_cor, y_cor)
        self.segments.append(snake)

    def move_forward(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[i - 1].xcor()
            y_cor = self.segments[i - 1].ycor()
            self.segments[i].goto(x_cor, y_cor)
        self.head.forward(20)

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
