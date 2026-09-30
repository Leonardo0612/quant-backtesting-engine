import turtle
import pandas
import csv

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day 25/US State Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("Day 25/US State Game/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed Correct", prompt="What's another state's name? ").title()

    if answer_state == "Exit":
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

missing_states = [item for item in all_states if item not in guessed_states]

new_data = pandas.DataFrame(missing_states, columns = ["States:"])
new_data.to_csv("Day 25/US State Game/states_to_learn.csv", index = False)
