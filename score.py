from turtle import Turtle
import requests
FONT = ("Arial", 24, "bold")

sheety_endpoint = "https://api.sheety.co/191ba8dc30bd621e8e24877df765fc35/game/workouts"
response = requests.get(url=sheety_endpoint, auth=("huyhuy", "huyhuy123"))
response.raise_for_status()
data = response.json()
highest_lst = [data["workouts"][i]['score'] for i in range(len(data["workouts"]))]


class Score(Turtle):
    score = 0
    highest_score = max(highest_lst)

    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"Score: {Score.score}, High Score: {Score.highest_score}", align="center", font=FONT)

    def increase(self):
        self.clear()
        Score.score += 1
        self.create()
