import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_list = []

player = Player()
car = CarManager()
score  = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()

    for c in car.all_cars:
        if c.distance(player) < 20:
            game_is_on = False
            score.game_over()


    if player.is_at_finish():
        player.go_to_start()
        car.level_up()
        score.increase_level()


screen.exitonclick()

