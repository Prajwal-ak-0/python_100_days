from turtle import Turtle,Screen

timmy = Turtle()

def move_for():
    timmy.forward(10)

def move_bck():
    timmy.backward(10)

def rot_anti():
    timmy.left(10)

def rot_clk():
    timmy.right(10)

def clr():
    timmy.clear()
    timmy.penup()
    timmy.home()

screen = Screen()
screen.listen()
screen.onkey(move_for,"w")
screen.onkey(move_bck,"s")
screen.onkey(rot_anti,"a")
screen.onkey(rot_clk,"d")
screen.onkey(clr,"c")
screen.exitonclick()