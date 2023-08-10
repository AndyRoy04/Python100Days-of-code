# from turtle import Turtle, Screen

# tom = Turtle()
# print(tom)
# tom.shape("turtle")
# tom.color("indigo")
# tom.forward(100)

# my_screen = Screen()
# a = my_screen.canvwidth
# print(a)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_autoindex("S/N")

table.align = "l"

print(table)