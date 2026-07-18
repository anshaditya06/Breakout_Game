import turtle as t
from paddle import Paddle
from ball import Ball

window = t.Screen()
window.title("Breakout Game")
window.bgcolor("black")
window.setup(width=800, height=600)


window.tracer(0)  # Turn off automatic screen updates

p = Paddle()
b = Ball(p)

def game_loop():
    b.move()
    b.bounce_wall_check()
    b.paddle_collision()
    b.reset_position()

    window.update()
    window.ontimer(game_loop, 10)


window.listen()
window.onkeypress(p.move_left, "Left")
window.onkeypress(p.move_right, "Right")

game_loop()
window.mainloop()
