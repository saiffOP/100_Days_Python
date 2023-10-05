# from turtle import Turtle, Screen
#
# Timmy = Turtle()
# Timmy.shape("turtle")
# Timmy.color("DarkGreen", "chocolate4")
# Timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable


table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)