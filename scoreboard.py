from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.write(arg=f"Score: {self.score}    High Score: {self.high_score}", align="center", font=("Arial", 30, "normal"))
        self.hideturtle()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_scoreboard()
        self.read_high_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align="center", font=("Arial", 30, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}    High Score: {self.high_score}", align="center", font=("Arial", 30, "normal"))

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_high_score(self):
        with open("data.txt", "w") as file:
            file.write(f"{self.high_score}")

    def read_high_score(self):
        with open("data.txt") as file:
            high_score = file.read()
            return high_score

