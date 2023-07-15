from turtle import Turtle


class Ball(Turtle) :
    def __init__(self) :
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.MOVE_X = 7
        self.MOVE_Y = 7
        self.move_speed=0.1
    
    def move(self) :
        x_cor=self.xcor() + self.MOVE_X
        y_cor=self.ycor() + self.MOVE_Y
        self.goto(x_cor,y_cor)
        
    def bounce_x(self) :
        self.MOVE_X *= -1
        self.move_speed *= 0.9

    def bounce_y(self) :
        self.MOVE_Y *= -1

    def reset_screen(self) :
        self.goto(0,0)
        self.bounce_x()
        self.move_speed=0.05
        