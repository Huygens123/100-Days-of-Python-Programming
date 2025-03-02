import turtle
import pandas as pd

data = pd.read_csv('50_states.csv')
screen = turtle.Screen()
screen.title('U.S State Game')
image = 'blank_states_img.gif'

screen.addshape(image)
turtle.shape(image)

# def get_coordinate(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_coordinate)
# turtle.mainloop()
# screen.exitonclick()

score = 0
state_list = data.state.to_list()
state_list_lower = []
Font = 'garamond', 8, 'bold'
data_state = data.state.to_list()
t = turtle.Turtle()

game_continue = True
wrong_answer_chance = 5
guessed_state = []

while game_continue and len(guessed_state) < 50:
    user_input = screen.textinput(title=f"{score}/50Guess the State",
                                  prompt="What is another State's name? ").title()
    if user_input == 'Exit':
        missing_states = [state for state in data_state if state not in guessed_state]
        # for state in data_state:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if user_input in data_state:
        score += 1
        guessed_state.append(user_input)
        x_cord, y_cord = data.loc[data.state == user_input, ['x', 'y']].values[0]
        t.penup()
        t.hideturtle()
        t.goto(x=x_cord
               , y=y_cord)
        t.write(user_input, font=Font)
    else:
        t.penup()
        t.hideturtle()
        wrong_answer_chance -= 1
        t.goto(x=-100, y=300)
        t.write(f"You have {wrong_answer_chance} more chances", font=('garamond', 20, 'bold'))
        t.clear()

    if wrong_answer_chance == 0:
        t.write('Game Over')
        game_continue = False
