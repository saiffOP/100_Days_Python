from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def clock_wise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def anti_clock_wise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clear_all():
    tim.home()
    tim.clear()
    

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=clock_wise)
screen.onkey(key="d", fun=anti_clock_wise)
screen.onkey(key="c", fun=clear_all)
screen.exitonclick()
