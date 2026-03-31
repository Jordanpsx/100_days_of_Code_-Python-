from turtle import Turtle, Screen
import random

def random_color():
    r = random.uniform(0, 1)
    g = random.uniform(0, 1)
    b = random.uniform(0, 1)

    return (r, g, b)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

timmy_the_turtle.pensize(5)
timmy_the_turtle.speed(5)
for i in range(random.randint(100,1000)):

    timmy_the_turtle.pencolor(random_color())

    num1 = random.randint(1, 4)
    timmy_the_turtle.right((360/4)*num1)
    timmy_the_turtle.forward(25)




screen = Screen()
screen.exitonclick()