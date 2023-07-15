import turtle as t
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen=t.Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Ping Pong Game")

r_paddle=Paddle((380,0))
l_paddle=Paddle((-380,0))
ball=Ball()
scoreboard=ScoreBoard()


screen.listen()
screen.onkeypress(r_paddle.move_paddle_up, "Up")
screen.onkeypress(r_paddle.move_paddle_down, "Down")
screen.onkeypress(l_paddle.move_paddle_up, "w")
screen.onkeypress(l_paddle.move_paddle_down, "s")

game_is_on=True
while game_is_on :
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Collison With Wall
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

    # Collision With Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350 :
        ball.bounce_x()
    
    # Whem Right Paddle Misses
    if ball.xcor() > 390 :
        scoreboard.update_score1()
        ball.reset_screen()

    # Whem Left Paddle Misses
    if ball.xcor() < -390 :
        scoreboard.update_score2()
        ball.reset_screen()

screen.exitonclick()
