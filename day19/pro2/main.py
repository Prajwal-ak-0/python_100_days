from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(500,400)

t = []
is_race_on = False
user_bet = screen.textinput("Make a bet","Name the color of turtle that is going to win the race ? :")
colors = ["red","orange","yellow","green","blue","purple"]

for i in range(6):
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.penup()
    timmy.color(colors[i-1])
    timmy.sety(i*30)
    timmy.setx(-230)
    t.append(timmy)

line = Turtle()
line.penup()
line.goto(230,180)
line.right(90)
line.pendown()
line.forward(200)
t.append(line)

t.pop(6)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in t:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've Lost! The {winning_color} turtle is the winner!")
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()