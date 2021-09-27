import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    tup = (r, g, b)
    return tup


screen = t.Screen()
tim = t.Turtle()
t.colormode(255)

angles = [0, 90, 180, 270]

tim.speed("fastest")
tim.pensize(10)

for _ in range(200):
    tim.forward(30)
    tim.pencolor(random_color())
    tim.seth(random.choice(angles))

screen.exitonclick()
