from turtle import Screen
from snake import Snake
from scoreboard import ScoreBoard
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

scoreboard = ScoreBoard()

increase_snake_speed_on = False
game_is_on = True
sleep_time = 0.05
while game_is_on:
    screen.update()
    time.sleep(0.1)   # Normal time is 0.1 or sleep_time
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()
        # The more you eat the slower you get
        if increase_snake_speed_on and sleep_time != 0.2:
            sleep_time += 0.002

    # Detect collision with wall.    Note: original wall distance was 280
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect collision with body.
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
