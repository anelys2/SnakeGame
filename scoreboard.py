from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.penup()

    def update_scoreboard(self):
        self.clear()
        self.reset_high_score()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def reset_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        #self.score = 0
        #self.update_scoreboard()
