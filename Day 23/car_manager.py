from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
class CarManager:

    def __init__(self):
        self.all_cars = []
        self.new_speed = 0
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        chance = random.randint(1, 10)
        if chance <= 2:
            new_car = Turtle('square')
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_cord = random.randint(-250, 250)
            new_car.goto(x=300, y=y_cord)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT




