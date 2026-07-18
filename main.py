import turtle as t
from paddle import Paddle
from ball import Ball
from brick import Brick

window = t.Screen()
window.title("Breakout Game")
window.bgcolor("black")
window.setup(width=800, height=600)


window.tracer(0)  # Turn off automatic screen updates





p = Paddle()




def create_bricks():
    bricks = []
    colors = ["red", "orange", "yellow", "green"]
    start_x = -350
    start_y = 250
    for row in range(4):
        for col in range(10):
            x = start_x + col * 76
            y = start_y - row * 25
            brick = Brick(x, y, colors[row])
            bricks.append(brick)
    return bricks

bricks = create_bricks()
b = Ball(p, bricks)


def game_loop():
    
    b.move()
    b.bounce_wall_check()
    b.paddle_collision()
    b.brick_collision(bricks)
    b.reset_position()

    window.update()
    window.ontimer(game_loop, 10)




window.listen()
window.onkeypress(p.move_left, "Left")
window.onkeypress(p.move_right, "Right")

game_loop()
window.mainloop()
