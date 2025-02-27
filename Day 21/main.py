import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)
l_paddle = Paddle((-370, 0))
r_paddle = Paddle((370, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.new_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or \
            ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()

    # Detect left paddle misses
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()


screen.exitonclick()
