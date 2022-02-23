from turtle import Screen
from pong import Paddle
from ball import Balls
from collide import Collision
from score import ScoreX
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
tim = Balls()
l_point = ScoreX((-300, 270))
r_point = ScoreX((185, 270))


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


switch = True
while switch:
    time.sleep(tim.move_speed)
    screen.update()
    tim.move()
    if tim.ycor() > 295 or tim.ycor() < -295:
        tim.bounce()

    if tim.distance(r_paddle) < 45 and tim.xcor() > 360:
        tim.bounce_x()
        r_point.increase()

    elif tim.distance(l_paddle) < 45 and tim.xcor() < -360:
        tim.bounce_x()
        l_point.increase()
    elif tim.xcor() > 380:
        tim.refresh()
        l_point.increase()
    elif tim.xcor() < -380:
        tim.refresh()
        r_point.increase()


screen.exitonclick()
