from turtle import Turtle
import random


class Apple(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.penup()
        self.goto(random.randint(-280, 280), random.randint(-220, 280))

    def new_apple(self):
        self.clear()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.penup()
        self.goto(random.randint(-280, 280), random.randint(-250, 280))