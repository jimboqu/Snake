from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

class_snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(class_snake.up, "Up")
screen.onkey(class_snake.down, "Down")
screen.onkey(class_snake.left, "Left")
screen.onkey(class_snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    class_snake.move()
    # detect collide with food
    if class_snake.head.distance(food) < 15:
        food.refresh()
        score.score_update()
        class_snake.extend()
    # detect collision with wall
    if class_snake.head.xcor() > 285 or class_snake.head.xcor() < -285 or class_snake.head.ycor() > 285 or class_snake.head.ycor() < -285:
        game_is_on = False
        score.game_over()
    for seg in class_snake.segments[1:]:
        if class_snake.head.distance(seg) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
# snake_list = []
# startpoint = 30
# for _ in range(3):
#     snake = Turtle("square")
#     snake.color("white")
#     snake.penup()
#     snake.goto(startpoint, 0)
#     snake_list.append(snake)
#     startpoint -= 20

# for seg in range(len(snake_list) -1, 0, -1):
#     new_x = snake_list[seg -1].xcor()
#     new_y = snake_list[seg -1].ycor()
#     snake_list[seg].goto(new_x, new_y)
# snake_list[0].forward(20)