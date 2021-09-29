import turtle as t

tim = t.Turtle()
screen = t.Screen()


def mov_forward():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=mov_forward)

screen.exitonclick()
