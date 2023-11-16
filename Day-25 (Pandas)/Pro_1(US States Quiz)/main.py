import turtle
import pandas
import time

screen = turtle.Screen()
screen.title("U.S States Quizz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

state = data.state.tolist()
x = data.x.tolist()
y = data.y.tolist()

game_on = True
answer_state = None

points = 0
score = turtle.Turtle()
score.hideturtle()
score.penup()
score.goto(0, 240)
def update_score():
    score.write(f"{points} / 50", align="center", font=("Courier", 30, "normal"))

update_score()

t = turtle.Turtle()
t.hideturtle()
t.penup()

while game_on:
    answer_state = screen.textinput("Guess the State", "What's another state's name?")

    if answer_state is None:
        break  # If the user clicks cancel in the input dialog

    for i in range(len(state)):
        if answer_state.lower() == state[i].lower():
            t.goto(x[i], y[i])
            t.write(state[i])
            points += 1
            score.clear()
            update_score()

            break  # Exit the loop once the correct state is found

    else:
        # This block will be executed if the loop didn't break (i.e., no matching state was found)
        t.goto(0, 0)
        t.write(f"{answer_state} is not one US State name. Re-enter.", align="center", font=("Courier", 16, "normal"))
        time.sleep(1)
        t.clear()

screen.exitonclick()
