from turtle import Screen, Turtle
screen = Screen()


def game_over():
    screen.clear()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake game")
    game_off = Turtle()
    game_off.penup()
    game_off.hideturtle()
    game_off.color("white")
    game_off.write("Game Over", align="center", font=("Arial", 24, "bold"))


