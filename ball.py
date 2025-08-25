from turtle import Turtle
import random
import winsound

INITIAL_HEADING = [45, 135, 225, 315]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.reset()
        self.speed(0)

    def bounce_wall(self):
        new_heading = 2 * (180 - self.heading()) + self.heading()
        self.setheading(new_heading)

    def bounce_paddle_left(self, paddle_x, paddle_y):
        if self.xcor() - paddle_x <= 20:
            if -50 <= self.ycor() - paddle_y <= 50:
                deflection_angle = 1.5 * (self.ycor() - paddle_y)
                self.setheading(360 + deflection_angle)
                winsound.Beep(1500, 100)
                return 1
            else:
                return 0
        else:
            return 0

    def bounce_paddle_right(self, paddle_x, paddle_y):
        if paddle_x - self.xcor() <= 20:
            if -50 <= self.ycor() - paddle_y <= 50:
                deflection_angle = 1.5 * (self.ycor() - paddle_y)
                self.setheading(180 - deflection_angle)
                winsound.Beep(1500, 100)
                return 1
            else:
                return 0
        else:
            return 0

    def reset(self):
        self.goto(0, random.randint(-100, 100))
        self.setheading(random.choice(INITIAL_HEADING))

