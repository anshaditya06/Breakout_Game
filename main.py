from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard

window = Screen()
window.title("Breakout Game")
window.bgcolor("black")
window.setup(width=800, height=600)


window.tracer(0)  # Turn off automatic screen updates

writer = Turtle()
writer.hideturtle()
writer.penup()
writer.color("white")

def display_start_screen():
    writer.goto(0, 0)
    writer.write("BREAKOUT\n\nClick to Start", align="center", font=("Courier", 24, "normal"))



def display_win_screen():
    writer.goto(0, 0)
    writer.write("YOU WIN!", align="center", font=("Courier", 24, "normal"))

def display_game_over_screen():
    writer.goto(0, 0)
    writer.write(f"GAME OVER\nFinal Score: {scoreboard.score}",
                 align="center", font=("Courier", 24, "normal"))
    

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
scoreboard = Scoreboard()
game_state = "start"


def start_game(x, y):
    global game_state
    if game_state == "start":
        writer.clear()
        game_state = "playing"

def game_loop():
    global game_state
    if game_state == "playing":
        b.move()
        b.bounce_wall_check()
        b.paddle_collision()
        if b.brick_collision(bricks):
            scoreboard.increase_score()
        if b.reset_position():
            if scoreboard.lose_life():
                game_state = "game_over"
                display_game_over_screen()
        if len(bricks) == 0:
            game_state = "win"
            display_win_screen()

    window.update()
    window.ontimer(game_loop, 10)

display_start_screen()
window.onclick(start_game)
game_loop()




window.listen()
window.onkeypress(p.move_left, "Left")
window.onkeypress(p.move_right, "Right")

game_loop()
window.mainloop()
