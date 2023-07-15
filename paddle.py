from turtle import Turtle

class Paddle(Turtle) :
    def __init__(self,position) :
        super().__init__("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.color("white")
        self.goto(position)

    def move_paddle_up(self) :
        y_cor=self.ycor()
        if y_cor < 260 :
            self.sety(y_cor+20)

    def move_paddle_down(self) :
        y_cor=self.ycor()
        if y_cor > -240 :
            self.sety(y_cor-20)

    