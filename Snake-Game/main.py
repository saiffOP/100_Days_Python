from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xenzia")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.new_score()

    # Detect Collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        new_game = screen.textinput("New Game", "Do you want to play a new game? Type 'yes' or 'no': ").lower()
        if new_game == "yes":
            score.reset_game()
            snake.reset_snake()
            screen.listen()
        else:
            game_is_on = False
            score.reset_game()
            game_over = Turtle()
            game_over.color("red")
            game_over.hideturtle()
            game_over.write("GAME OVER!", move=False, align="center", font=("Times New Roman", 24, "normal"))

    # Detect Collision with Tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            new_game = screen.textinput("New Game", "Do you want to play a new game? Type 'yes' or 'no': ").lower()
            if new_game == "yes":
                score.reset_game()
                snake.reset_snake()
                screen.listen()
            else:
                game_is_on = False
                score.reset_game()
                game_over = Turtle()
                game_over.color("red")
                game_over.hideturtle()
                game_over.write("GAME OVER!", move=False, align="center", font=("Times New Roman", 24, "normal"))

screen.exitonclick()
