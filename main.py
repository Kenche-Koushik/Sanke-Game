from turtle import Screen
from snake import Snake
from Food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=400, height=400)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 180 or snake.head.xcor() < -190 or snake.head.ycor() > 190 or snake.head.ycor() < -180:
        scoreboard.game_over()
        game_is_on = False

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()