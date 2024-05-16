"""
FUNCTION
"""
turn_left = 0
move = 0
front_is_clear = 0
right_is_clear = 0
at_goal = 0

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while at_goal() is False:
    if front_is_clear() is True:
        move()
    else:
        turn_left()
        move()
        if right_is_clear() is True:
            turn_right()
            move()
            turn_right()
        else:
            move()
            turn_right()
            move()
            if front_is_clear() is True:
                move()
            else:
                turn_right()
                if front_is_clear() is False:
                    turn_left()
                    move()
                else:
                    move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    if front_is_clear():
        move()
    else:
        turn_right()
        move()
        turn_right()
        move()
        turn_left()


while not at_goal():
    if not front_is_clear():
        jump()
    else:
        move()



