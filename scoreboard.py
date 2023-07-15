from turtle import Turtle

class ScoreBoard(Turtle) :
    def __init__(self) :
        self.score_1 = 0
        self.score_2 = 0
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,220)
        self.write_score()

    def write_score(self) :
        self.write(arg=f"{self.score_1}       ",align="center",font=("Arial",50,"bold"))
        self.write(arg=f"       {self.score_2}",align="center",font=("Arial",50,"bold"))
    
    def update_score1(self) :
        self.score_1 += 1
        self.clear()
        self.write_score()
        
    def update_score2(self) :
        self.score_2 += 1
        self.clear()
        self.write_score()
