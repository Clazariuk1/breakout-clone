import turtle as tr
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from ui import UI
from bricks import Bricks
import time


screen = tr.Screen()
screen.setup(width=1200, height=600)
screen.bgcolor('black')
screen.title('BREAKOUT')
screen.tracer(0)

ui = UI()
ui.header()

score = Scoreboard(lives=5)
paddle = Paddle()
bricks = Bricks()
ball = Ball()

game_paused = False
playing_game = True

def pause_game():
    global game_paused
    if game_paused:
        game_paused = False
    else:
        game_paused = True

screen.listen()
screen.onkey(key='Left', fun=paddle.move_left)
screen.onkey(key='Right', fun=paddle.move_right)
screen.onkey(key='space', fun=pause_game)

def check_collision_with_walls():

    global ball, score, playing_game, ui

    # detect collision with walls on left and right sides.
    if ball.xcor() < -580 or ball.xcor() > 570:
        ball.bounce(x_bounce=True, y_bounce=False)
        return
    # detect collision with wall at top
    if ball.ycor() > 270:
        ball.bounce(x_bounce=False, y_bounce=True)
        return

    # detect collision with BOTTOM wall
    # this will lose a life / reset game
    if ball.ycor() < -280:
        ball.reset()
        score.decrease_lives()
        if score.lives == 0:
            score.reset()
            playing_game = False
            ui.game_over(win=False)
            return
        ui.change_color()
        return

def check_collision_with_paddle():

    global ball, paddle
    #record x-axis coordinates of ball and paddle
    paddle_x = paddle.xcor()
    ball_x = ball.xcor()

    # check if ball's distance (at its middle) is less than width of paddle
    # and that ball is below a certain coordinate to detect the collision
    if ball.distance(paddle) < 110 and ball.ycor() < -250:

        # if Paddle is at right side of screen
        if paddle_x > 0:
            if ball_x > paddle_x:
                # if ball hits left side of paddle it moves left
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return
        # if Paddle is at LEFT of screen
        elif paddle_x < 0:
            if ball_x < paddle_x:
                # if ball hits paddle's left side, it moves back toward the left
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return
        # OR ELSE the paddle is in the middle horizontally, ball only vertical bounces
        else:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            elif ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return


def check_collision_with_bricks():
    global ball, score, bricks

    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            score.increase_score()
            brick.quantity -= 1
            if brick.quantity == 0:
                brick.clear()
                brick.goto(3000, 3000)
                bricks.bricks.remove(brick)

            # Detect collision from left
            if ball.xcor() < brick.left_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            # Detect collision from right
            elif ball.xcor() > brick.right_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            # Detect collision from bottom
            elif ball.ycor() < brick.bottom_wall:
                ball.bounce(x_bounce=False, y_bounce=True)

            # Detect collision from top
            elif ball.ycor() > brick.upper_wall:
                ball.bounce(x_bounce=False, y_bounce=True)


while playing_game:

    if not game_paused:

        # update the screen with all motion
        # that has happened

        screen.update()
        time.sleep(0.01)
        ball.move()

        # detect collision with walls
        check_collision_with_walls()

        # detect collision with paddle
        check_collision_with_paddle()

        # detect collision with bricks
        check_collision_with_bricks()

        # Detecting user victory
        if len(bricks.bricks) == 0:
            ui.game_over(win=True)
            break
    else:
        ui.paused_status()

tr.mainloop()
