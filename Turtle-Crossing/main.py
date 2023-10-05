import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Player Setup
player = Player()

# Car
cars = CarManager()

# ScoreBoard
scoreboard = Scoreboard()

# Listen to Key
screen.listen()
screen.onkey(player.move_player, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()

    # Detect Collision with Cars
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect Successful Crossing
    if player.is_at_finish_line():
        player.goto_start()
        cars.level_up()
        scoreboard.new_score()


screen.exitonclick()
