from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

# Right Paddle Setup
right_paddle = Paddle()
right_paddle.penup()
right_paddle.goto(x=350, y=0)


# Left Paddle Setup
left_paddle = Paddle()
left_paddle.penup()
left_paddle.goto(x=-350, y=0)


# Ball Setup
ball = Ball()

# ScoreBoard
scoreboard = ScoreBoard()

# Border
border = Turtle()
border.color("white")
border.penup()
border.goto(0, 300)
for _ in range(20):
    border.setheading(270)
    border.pendown()
    border.forward(30)
    border.penup()
    border.forward(30)

border.hideturtle()


screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collision with Right Paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect Collision with Left Paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect Right Paddle Miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect Left Paddle Miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
