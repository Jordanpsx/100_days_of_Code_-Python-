from turtle import Turtle, Screen
import random

def random_color():
    r = random.uniform(0, 1)
    g = random.uniform(0, 1)
    b = random.uniform(0, 1)

    return (r, g, b)

timmy_the_turtle = Turtle()
timmy_the_turtle.color("green")


timmy_the_turtle.pensize(2)
timmy_the_turtle.speed(100)

for i in range(36):

    timmy_the_turtle.pencolor(random_color())

    timmy_the_turtle.circle(100)
    timmy_the_turtle.right(10)




screen = Screen()
screen.exitonclick()