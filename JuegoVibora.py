"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import update, clear, setup, hideturtle, \
    tracer, onkey, done, listen, ontimer
from random import randint
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    snake.append(head)

    if head == food:
        print('Snake:',  len(snake))
        rand_num = randint(0, 10)

        if 0 <= rand_num <= 2:
            food.x = (food.x + 10)
            food.y = (food.y + 10)

        elif 3 <= rand_num <= 5:
            food.x = (food.x - 10)
            food.y = (food.y - 10)

        elif 6 <= rand_num <= 8:
            food.x = (food.x + 10)
            food.y = (food.y - 10)

        elif 9 <= rand_num <= 10:
            food.x = (food.x - 10)
            food.y = (food.y + 10)

        if food.x >= 150 or food.y >= 150 or food.x <= -150 or food.y <= -150:
            food.x = 0
            food.y = 0

    else:
        snake.pop(0)
    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')
    square(food.x, food.y, 9, 'green')
    update()

    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
