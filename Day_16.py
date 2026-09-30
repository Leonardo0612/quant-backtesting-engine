# from turtle import Turtle, Screen

# Leon = Turtle()
# print(Leon)
# Leon.shape("turtle")
# Leon.color("coral")
# Leon.pencolor("red")
# Leon.pensize(10)
# def heart():
#     Leon.left(135)
#     Leon.forward(50)
#     Leon.circle(85, 180)
#     Leon.forward(220)
#     Leon.left(90)
#     Leon.forward(220)
#     Leon.circle(85, 180)
#     Leon.forward(50)
#     Leon.right(135)
# heart()
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

my_table = PrettyTable()
my_table.field_names = ["Pokemon Name", "Type"]
my_table.add_row(["Pikachu", "Electric"], divider = True)
my_table.add_row(["Squirtle", "Water"], divider = True)
my_table.add_row(["Charmander", "Fire"], divider = True)
my_table.add_row(["Bulbasaur", "Grass"])

my_table.align["Pokemon Name"] = "l"
print(my_table)
