from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        y_move = self.ycor() + 10
        self.goto(0, y_move)

    def finish_line(self):
        y_cord = FINISH_LINE_Y
        if self.ycor() == y_cord:
            self.goto(STARTING_POSITION)

