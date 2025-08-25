from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from centerline import Centerline
import time
import math
import winsound

INITIAL_SPEED = 10
SLEEP_TIME = 0.05

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle(position=(-380, 0))
right_paddle = Paddle(position=(380, 0))
ball = Ball()
left_scoreboard = Scoreboard(position=(-50, 260))
right_scoreboard = Scoreboard(position=(50, 260))
centerline = Centerline()


screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

speed_multiplier = 1
hit_counter = 0

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(SLEEP_TIME)
    heading = ball.heading()
    speed = int(abs(INITIAL_SPEED * speed_multiplier / math.cos(math.radians(ball.heading()))))
    ball.forward(speed)

    # Detect collision with paddles
    hit_counter += ball.bounce_paddle_left(left_paddle.xcor(), left_paddle.ycor())
    hit_counter += ball.bounce_paddle_right(right_paddle.xcor(), right_paddle.ycor())
    speed_multiplier = 1 + 0.2 * hit_counter

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
        winsound.Beep(1000, 100)

    # Detect passing goal
    if ball.xcor() > 400:
        left_scoreboard.gain_point()
        hit_counter = 0
        speed_multiplier = 1
        ball.reset()
        winsound.Beep(200, 1000)

    if ball.xcor() < -400:
        right_scoreboard.gain_point()
        hit_counter = 0
        speed_multiplier = 1
        ball.reset()
        winsound.Beep(200, 1000)


    # Detect game over
    if left_scoreboard.score == 11 or right_scoreboard.score == 11:
        game_is_on = False
        left_scoreboard.game_over()



screen.exitonclick()