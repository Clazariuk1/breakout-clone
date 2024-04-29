from turtle import Turtle
MOVE_DIST = 2

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move_dist = MOVE_DIST
        self.y_move_dist = MOVE_DIST
        self.reset()

    def move(self):
        #move TEN steps ahead, vertically and horizontally
        new_y = self.ycor() + self.y_move_dist
        new_x = self.xcor() + self.x_move_dist
        self.goto(x=new_x, y=new_y)

    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            #REVERSE horizontal direction
            self.x_move_dist *= -1
        if y_bounce:
            #reverse the VERTICAL direction
            self.y_move_dist *= -1

    def reset(self):
        #ball should go to an initial position and will always start with UPWARD movement
        self.goto(x=0, y=-240)
        self.y_move_dist = 10
