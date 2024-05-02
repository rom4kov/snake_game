import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
scoreboard.print_press_space()


def start_game():
    game_is_on = True
    scoreboard.write_score()
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.add_score_point()
            snake.grow()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset()
            snake.reset()
            game_is_on = False
            scoreboard.print_press_space()

        for part in snake.body[2:]:
            if snake.head.distance(part) < 10:
                scoreboard.reset()
                snake.reset()
                game_is_on = False
                scoreboard.print_press_space()


screen.update()

screen.listen()
screen.onkey(fun=start_game, key="space")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

screen.exitonclick()
