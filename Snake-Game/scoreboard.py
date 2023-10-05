from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Times New Roman", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.HighScore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.HighScore}", move=False, align=ALIGNMENT, font=FONT)

    def new_score(self):
        self.score += 1
        self.update_score()

    def reset_game(self):
        if self.score > self.HighScore:
            self.HighScore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.HighScore}")
        self.score = 0
        self.update_score()

