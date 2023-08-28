from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Times New Roman", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", move=False, align=ALIGNMENT, font=FONT)

    def new_score(self):
        self.score += 1
        self.clear()
        self.update_score()
