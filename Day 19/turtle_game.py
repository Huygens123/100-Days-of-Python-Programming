import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=300)
user_pred = screen.textinput(title="Make your Prediction", prompt="Which turtle will win the game? Enter a color")

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-120, -80, -40, 0, 40, 80, 120]
all_turtle = []

for turtle in range(0, 6):
    new_turtle = Turtle('turtle')
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle])
    new_turtle.forward(random.randint(0, 10))
    all_turtle.append(new_turtle)

if user_pred:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_pred:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
