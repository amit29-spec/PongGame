from turtle import Turtle


class Collision(Turtle):
    def __init__(self):
        super().__init__()

    def go_up(self):
        new_y = self.ycor() + 80
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 80
        self.goto(self.xcor(), new_y)