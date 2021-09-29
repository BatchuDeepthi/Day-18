import turtle  as t

tim = t.Turtle()
screen = t.Screen()


def mov_fwd():
    tim.forward(10)


def mov_bckwd():
    tim.backward(10)


def turn_left():
    current_heading =  tim.heading()+10
    tim.setheading(current_heading)



def turn_right():
    current_heading =  tim.heading()-10
    tim.setheading(current_heading)


screen.listen()
screen.onkeypress(key="w", fun=mov_fwd)
screen.onkey(key="s", fun=mov_bckwd)
screen.onkey(key="c", fun=tim.reset)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)

screen.exitonclick()
