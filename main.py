import time
import requests
from turtle import Screen
from score import Score
from apple import Apple
from snake import Snake
from game_over import game_over
from datetime import datetime as dt

# Create a datetime now module
now = dt.now()
today = now.strftime("%d/%m/%Y")
time_line = now.strftime("%X")

# Create a function to pass into Sheety post module


def parameter(day, time_line, name, score):
    params = {
        "workout": {
            'date': day,
            'time': time_line,
            'name': name,
            'score': score
        }
    }
    return params


# Create screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
name_user = screen.textinput(title="User name", prompt="Enter your name").title()
screen.tracer(0)

# Create objects
apple = Apple()
snake = Snake()
score = Score()

# Create a key_control
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Sheety module
sheety_endpoint = "https://api.sheety.co/191ba8dc30bd621e8e24877df765fc35/game/workouts"
game_on = True
while game_on:
    screen.update()
    time.sleep(0.09)
    # always move forward
    snake.move_forward()

    # if hit the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_over()
        params = parameter(today, time_line, name_user, Score.score)
        user_response = requests.post(url=sheety_endpoint, json=params, auth=("huyhuy", "huyhuy123"))
        game_on = False

    # if snake ate an apple
    if snake.head.distance(apple) < 18:
        apple.new_apple()
        score.increase()
        snake.increase()

    # if snake ate itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_over()
            params = parameter(today, time_line, name_user, Score.score)
            user_response = requests.post(url=sheety_endpoint, json=params, auth=("huyhuy", "huyhuy123"))
            game_on = False

screen.exitonclick()

