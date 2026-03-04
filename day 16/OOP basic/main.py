# from turtle import Turtle, Screen
#
# tortuga = Turtle()
#
# tortuga.color("chartreuse4")
# tortuga.shape("turtle")
# tortuga.forward(100)
#
# my_screen = Screen()
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.field_names= ["Pokemon Name", "type"]
table.add_rows(
    [
        ["Pikachu", "Eletric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)

print(table)

table.align = "l"

print(table)