from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Times New Roman", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(-240, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER!", move=False, align=ALIGNMENT, font=("Times New Roman", 48, "normal"))

    def new_score(self):
        self.score += 1
        self.clear()
        self.update_score()

