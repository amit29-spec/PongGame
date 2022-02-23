from turtle import Turtle


class ScoreX(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.write(f"SCORE = {self.score}", False, align="left", font=("Arial", 16, "normal"))

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE = {self.score}", False, align="left", font=("Arial", 16, "normal"))
