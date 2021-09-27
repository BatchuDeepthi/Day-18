from turtle import Turtle, Screen
import random

tim = Turtle()
colors = ['brown', 'blue', 'green', 'pink', 'red', 'yellow', 'gold', 'lavender','violet','orange']
screen = Screen()


def draw_shape(num_of_sides):
    tim.pencolor(random.choice(colors))
    angle = 360/num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)


for sides in range(3,11):
    draw_shape(sides)



screen.exitonclick()
