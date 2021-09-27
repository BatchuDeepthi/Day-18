import turtle as t
import random

colors = [(250, 246, 243), (248, 245, 246), (212, 154, 98), (242, 249, 247), (236, 241, 245), (53, 107, 131),
          (199, 142, 34), (178, 78, 33), (116, 156, 171), (124, 79, 98), (123, 175, 157), (226, 198, 129),
          (190, 88, 109), (12, 49, 64), (56, 39, 19), (40, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30),
          (225, 93, 78), (244, 163, 160), (38, 32, 34), (3, 25, 25), (79, 147, 169), (163, 26, 21), (19, 79, 91),
          (235, 166, 170), (171, 207, 190), (102, 127, 158), (163, 203, 211)]


def draw_line():
    for i in range(10):
        tim.color(random.choice(colors))
        tim.dot(10)
        tim.penup()
        if i != 9:
            tim.forward(0.5)


t.colormode(255)
tim = t.Turtle()
screen = t.Screen()


screen.setworldcoordinates(0, 0, 9, 9)

for i in range(10):
    draw_line()
    if i == 9:
        pass
    else:
        if i % 2 == 0:
            tim.left(90)
            tim.forward(0.5)
            tim.left(90)
        else:
            tim.right(90)
            tim.forward(0.5)
            tim.right(90)
    tim.dot(10)
    
tim.hideturtle()

screen.exitonclick()
