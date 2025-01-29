from turtle import Turtle ,Screen
import time
from snake import Snake
from food import Food


screen = Screen()
screen.tracer(0)
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("🐍🐍 Snake Game 🐍🐍")


food = Food()
snake = Snake()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True 

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

#Collision with food 

    if snake.head.distance(food) < 15:
        food.refresh()



screen.exitonclick()