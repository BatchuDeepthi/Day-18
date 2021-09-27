from turtle import Turtle,Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

screen = Screen()

for i in range(4):
    timmy.forward(100)
    timmy.right(90)

for i in range(15):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
screen.exitonclick()