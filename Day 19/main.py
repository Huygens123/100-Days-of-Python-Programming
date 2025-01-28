from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def backwards():
    tim.backward(10)

def counter_clockwise_move():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clockwise_move():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=backwards)
screen.onkey(key='a', fun=counter_clockwise_move)
screen.onkey(key='d', fun=clockwise_move)
screen.onkey(key='c', fun=clear)


screen.exitonclick()
