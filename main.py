import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
img = "blank_states_img.gif"

screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

states_guessed = 0
correct_guesses = []

while states_guessed < 50:
    user_answer = screen.textinput(title=f"{states_guessed}/50 States Correct",
                                   prompt="What's another state's name?").title()
    if user_answer == "Exit":
        states_to_learn = [state for state in all_states if state not in correct_guesses]

        states_to_learn_df = pandas.DataFrame(states_to_learn)
        states_to_learn_df.to_csv("states_to_learn.csv")

        break

    if user_answer in all_states:
        # print("correct")
        correct_guesses.append(user_answer)
        states_guessed += 1

        state_data = data[data["state"] == user_answer]
        state_data_i = state_data.index[0]
        x = int(state_data["x"][state_data_i])
        y = int(state_data["y"][state_data_i])

        answer = turtle.Turtle()
        answer.hideturtle()
        answer.penup()
        answer.goto(x, y)
        answer.write(user_answer, align="center", font=("Arial", 8, "normal"))



# gets the x and y coordinates of the mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor) # calls the function when the mouse is clicked on the screen


# turtle.mainloop() # keeps the window open until it is closed

# screen.exitonclick() # closes the window when clicked