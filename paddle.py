import turtle as t
class Paddle:
    def __init__(self):
        self.paddle = t.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.penup()
        self.paddle.goto(0, -250)

    def move_left(self):
        x = self.paddle.xcor()
        x -= 30
        if x < -350:  # Prevent the paddle from going off the left edge
            x = -350
        self.paddle.setx(x)

    def move_right(self):
        x = self.paddle.xcor()
        x += 30
        if x > 350:  # Prevent the paddle from going off the right edge
            x = 350
        self.paddle.setx(x)

