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

tim.speed("fastest")
current_heading = tim.heading()

while current_heading <= 360:
    tim.color(random_color())
    tim.circle(100)
    tim.seth(current_heading)
    current_heading += 5

screen.exitonclick()