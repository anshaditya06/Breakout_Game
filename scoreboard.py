from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-380, 260)  # top-left corner, adjust to your screen
        self.update_display()

    def update_display(self):
        self.clear()
        self.write(f"Score: {self.score}   Lives: {self.lives}",
                    align="left", font=("Courier", 16, "normal"))

    def increase_score(self, points=1):
        self.score += points
        self.update_display()

    def lose_life(self):
        self.lives -= 1
        self.update_display()
        return self.lives <= 0  # True means game over