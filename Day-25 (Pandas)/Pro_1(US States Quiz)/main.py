import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Quizz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.



answer_state = screen.textinput("Guess the State","What's another state's name?")

screen.exitonclick()