from turtle import Turtle

class Centerline(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(0, -290)
        self.setheading(90)
        self.shapesize(stretch_wid=0.5, stretch_len=2)
        for _ in range(8):
            self.stamp()
            self.forward(80)


