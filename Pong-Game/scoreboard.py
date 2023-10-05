from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Times New Roman", 40, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.goto(-100, 240)
        self.write(self.l_score, move=False, align=ALIGNMENT, font=FONT)
        self.goto(100, 240)
        self.write(self.r_score, move=False, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", move=False, align=ALIGNMENT, font=FONT)
