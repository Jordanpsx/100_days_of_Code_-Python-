from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

for i in range(8):
    num1 = random.uniform(0, 1)
    num2 = random.uniform(0, 1)
    num3 = random.uniform(0, 1)
    timmy_the_turtle.pencolor(num1, num2, num3)

    for n in range(i+3):
        timmy_the_turtle.right(360/(i+3))
        timmy_the_turtle.forward(100)


screen = Screen()
screen.exitonclick()