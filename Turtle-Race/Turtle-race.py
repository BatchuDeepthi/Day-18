import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a colour:")
colors = ['red','yellow','green','orange','purple','blue']
all_turtles =[]

if user_bet:
    is_race_on = True

for i in range(6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-80 + i * 30)
    all_turtles.append(new_turtle)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            actual_win = turtle.pencolor()
            if user_bet == actual_win:
                print(f'You win')
            else:
                print(f'You lose.{actual_win4} turtle won the race')
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()