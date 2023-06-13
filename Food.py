from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        random_x = random.randint(-160, 160)
        random_y = random.randint(-160, 150)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-160, 160)
        random_y = random.randint(-160, 160)
        self.goto(random_x, random_y)