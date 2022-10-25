from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake

start = True

def play_again():
    global start
    restart = screen.textinput("Do you wish to start?", "YES or NO")

    if restart == "YES" or restart == "yes" or restart == "Yes":
        screen.clear()
        start = True
    else:
        start = False
        screen.bye()

while start:

    screen = Screen()
    screen.colormode(255)
    screen.setup(height=600, width=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(n=0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_on = True

    while game_on:
        scoreboard.update_scoreboard()
        screen.update()
        time.sleep(0.1)
        snake.move()

        #Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        #Detect collision with walls
        if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
            # game_on = False
            scoreboard.game_over()
            game_on = False
            play_again()

        #Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                game_on = False
                play_again()



#screen.exitonclick()