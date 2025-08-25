from turtle import Turtle
MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.speed(0)
        self.goto(position)
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()

    def up(self):
        if self.ycor() < 240:
            self.forward(MOVE_DISTANCE)

    def down(self):
        if self.ycor() > -220:
            self.backward(MOVE_DISTANCE)


