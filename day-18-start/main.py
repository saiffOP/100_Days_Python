import turtle
from turtle import Turtle, Screen
import random


turtle.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour_tuple = (r, g, b)
    return colour_tuple


angle = [0, 90, 180, 270]
timmy = Turtle()
timmy.shape("turtle")
timmy.color("green", "chocolate4")
timmy.speed("fastest")


# POLYGONS
# for num_of_sides in range(3, 11):
#     timmy.color(random.choice(colours))
#     for _ in range(num_of_sides):
#         timmy.pensize(5)
#         angle = 360 / num_of_sides
#         timmy.forward(100)
#         timmy.right(angle)


# Random Walk
# count = 0
# while count <= 50:
#     timmy.pensize(10)
#     timmy.color(random_colour())
#     timmy.forward(30)
#     timmy.right(random.choice(angle))
#     count += 1


# Spirograph

# def Spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         timmy.color(random_colour())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size_of_gap)
#
#
# Spirograph(5)


# Hirst Painting

timmy.penup()
timmy.hideturtle()
timmy.goto(-250, 250)
# for i in range(10):
#     for j in range(10):
#         timmy.dot(20, random_colour())
#         timmy.penup()
#         timmy.forward(50)
#     timmy.goto(-250, timmy.ycor() - 50)

for i in range(10):
    for j in range(10):
        timmy.dot(20, random_colour())
        timmy.penup()
        timmy.forward(50)
    timmy.setheading(270)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)

timmy.hideturtle()



screen = Screen()
screen.exitonclick()
