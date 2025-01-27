import turtle
from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('arrow')
timmy_the_turtle.shapesize(1.0, 1.0, 1)
timmy_the_turtle.color('coral')
# timmy_the_turtle.forward(200)
# timmy_the_turtle.left(90)
# timmy_the_turtle.back(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.back(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.back(200)

# for _ in range(4):
#     timmy_the_turtle.forward(200)
#     timmy_the_turtle.right(90)

# for _ in range(15):
#     timmy_the_turtle.pensize(1)
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(20)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
# def shape(side):
#     angle = 360 / side
#     for _ in range(side):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#
# for _ in range(3, 11):
#     timmy_the_turtle.color(random.choice(colours))
#     shape(_)

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


# direction = [0, 90, 180, 270]
#
# for move in range(500):
#     timmy_the_turtle.speed('fastest')
#     timmy_the_turtle.pencolor((random_color()))
#     timmy_the_turtle.pensize(20)
#     timmy_the_turtle.forward(50)
#     timmy_the_turtle.setheading(random.choice(direction))
def draw_spiral(spiral_gap):

    for _ in range(int(360/spiral_gap)):
        timmy_the_turtle.speed('fastest')
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + spiral_gap)


draw_spiral(5)



screen = Screen()
screen.exitonclick()
