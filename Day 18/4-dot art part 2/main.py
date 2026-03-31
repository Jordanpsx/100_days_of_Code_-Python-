from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
color_list = [(102, 153, 255), (255, 204, 153), (199, 175, 118), (125, 36, 24),
              (187, 158, 50), (170, 105, 56), (5, 57, 83), (153, 255, 204), (204, 255, 153), (108, 67, 85), (39, 36, 35)]
timmy_the_turtle.speed(1)

def random_color():

    r, g, b = random.choice(color_list)
    new_color = (r / 255, g / 255, b / 255)
    return new_color

for i in range(10):


    for n in range(10):
        timmy_the_turtle.pendown()
        timmy_the_turtle.pencolor(random_color())
        timmy_the_turtle.dot(20)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(50)

    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(50)
    timmy_the_turtle.left(90)
    timmy_the_turtle.teleport(0)
    timmy_the_turtle.right(180)

screen = Screen()
screen.exitonclick()