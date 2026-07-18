import turtle as t

from paddle import Paddle


class Ball(Paddle):
    def __init__(self, paddle):
        self.paddle = paddle
        self.ball = t.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("red")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.dx = 2
        self.dy = -2



    def move(self):
        self.ball.setx(self.ball.xcor() + self.dx)
        self.ball.sety(self.ball.ycor() + self.dy)

    def paddle_collision(self):
        paddle_turtle = self.paddle.paddle
        if (
            self.ball.ycor() < paddle_turtle.ycor() + 20
            and paddle_turtle.xcor() - 60 < self.ball.xcor() < paddle_turtle.xcor() + 60
        ):
            self.dy *= -1

    def bounce_wall_check(self):
        if self.ball.xcor() > 380 or self.ball.xcor() < -380:
            self.dx *= -1
        if self.ball.ycor() > 280:
            self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def bounce_y(self):
        self.dy *= -1

    def reset_position(self):
        if self.ball.ycor() < -300 or self.ball.ycor() > 300:
            self.ball.goto(0, 0)
            self.dx = 2
            self.dy = -2