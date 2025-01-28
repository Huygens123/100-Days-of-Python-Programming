from turtle import Turtle, Screen

turtle = Turtle('arrow')
screen = Screen()


def up():
    turtle.setheading(90)


def down():
    turtle.setheading(270)

def left():
    turtle.setheading(180)


def right():
    turtle.setheading(360)

for num in range(20):
    turtle.forward(20)


screen.listen()
screen.onkey(up, 'Up')
screen.onkey(down, 'Down')
screen.onkey(left, 'Left')
screen.onkey(right, 'Right')

screen.exitonclick()