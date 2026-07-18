import turtle as t
from paddle import Paddle
from ball import Ball

window = t.Screen()
window.title("Breakout Game")
window.bgcolor("black")
window.setup(width=800, height=600)


window.tracer(0)  # Turn off automatic screen updates

game_over = False

p = Paddle()
b = Ball(p)

def game_loop():
    global game_over

    if game_over:
        window.update()
        window.ontimer(game_loop, 10)
        return

    b.move()
    b.bounce_wall_check()
    b.paddle_collision()
    if not b.reset_position():
        display_game_over_screen()

    window.update()
    window.ontimer(game_loop, 10)

writer = t.Turtle()
writer.hideturtle()
writer.color("white")
writer.penup()

def display_game_over_screen():
    global game_over
    game_over = True
    writer.clear()
    writer.goto(0, 0)
    writer.write("Game Over - Click to Restart", align="center", font=("Courier", 24, "normal"))
    window.onscreenclick(restart_game)


def restart_game(x, y):
    global game_over
    writer.clear()
    b.reset_position()
    p.reset_position()
    game_over = False
    # reset score/lives too if you're tracking them


window.listen()
window.onkeypress(p.move_left, "Left")
window.onkeypress(p.move_right, "Right")

game_loop()
window.mainloop()
