from turtle import Turtle, Screen
import random

screen = Screen()
tim = Turtle()
colors = ['brown', 'blue', 'green', 'pink', 'red', 'yellow', 'gold', 'lavender', 'violet', 'orange']
angles = [0, 90, 180, 270]

for _ in range(200):
    tim.speed("fast")

    tim.pensize(10)
    tim.forward(30)
    tim.pencolor(random.choice(colors))
    tim.seth(random.choice(angles))

    tim.fillcolor(random.choice(colors))

screen.exitonclick()
