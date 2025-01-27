# import colorgram
#
# colors = colorgram.extract('R.jpeg', 30)
#
# color_all = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     color_all.append(rgb)
import random
# print(color_all)

import turtle as t
color_list = [(196, 166, 105), (133, 167, 194), (46, 103, 147), (147, 89, 40), (9, 21, 54), (189, 156, 33),
              (225, 208, 112), (62, 22, 9), (68, 120, 77), (58, 12, 23), (185, 140, 166), (136, 181, 149),
              (136, 28, 12), (132, 76, 105), (14, 43, 26), (18, 53, 137), (121, 26, 41), (170, 101, 137), (92, 152, 97),
              (175, 189, 217), (86, 121, 184), (22, 93, 65), (67, 153, 170), (184, 99, 86), (210, 177, 204),
              (89, 77, 15)]

point = t.Turtle()
point.hideturtle()
t.colormode(255)
point.speed('fastest')
point.penup()
point.setheading(225)
point.forward(500)
point.setheading(0)
no_of_dots = 1000
point.pensize(1)


for move in range(1, no_of_dots + 1):
    point.dot(10, random.choice(color_list))
    point.forward(50)

    if move % 10 == 0:
        point.left(90)
        point.penup()
        point.forward(50)
        point.left(90)
        point.forward(500)
        point.setheading(0)


screen = t.Screen()
screen.screensize(500, 500)
screen.exitonclick()
