import turtle
import random

# Create screen
screen = turtle.Screen()

# Create list of turtles
turtles = []
for i in range(10):
    t = turtle.Turtle()
    t.penup()
    turtles.append(t)

# Generate random coordinates
coordinates = []
for i in range(10):
    x = random.uniform(-180, 180)
    y = random.uniform(-90, 90)
    coordinates.append((x, y))

# Move turtles to coordinates
for i in range(len(turtles)):
    turtles[i].goto(coordinates[i])

# Keep screen open
screen.mainloop()
