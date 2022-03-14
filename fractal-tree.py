import turtle

# How many recursions you want the tree to have
tree_depth = 9

# Size of the canvas
canv_length = 300

# Size of the base trunk
trunk_length = 80

# How little you want each recursion to shrink
ratio = 7 / 8

# Orientations
east = 0
north = 90
west = 180
south = 270

my_screen = turtle.Screen()
my_screen.screensize(canv_length, canv_length, '#2d2d2d')

my_turtle = turtle.Turtle()
my_turtle.pencolor('white')
my_turtle.width(3)
my_turtle.hideturtle()

# Set the direction you want to grow the tree
my_turtle.setheading(north)

my_turtle.penup()
if (my_turtle.heading() == east):
    my_turtle.setx(-1 * canv_length / 2)
elif (my_turtle.heading() == north):
    my_turtle.sety(-1 * canv_length / 2)
elif (my_turtle.heading() == west):
    my_turtle.setx(canv_length / 2)
elif (my_turtle.heading() == south):
    my_turtle.sety(canv_length / 2)
my_turtle.pendown()

def drawTree(n, length):
    if (n == 1):
        my_turtle.forward(length)
        my_turtle.penup()
        my_turtle.backward(length)
        my_turtle.pendown()
    else:
        my_turtle.forward(length)
        my_turtle.left(15)
        drawTree(n - 1, ratio * length)
        my_turtle.right(30)
        drawTree(n - 1, ratio * length)
        my_turtle.left(15)
        my_turtle.penup()
        my_turtle.backward(length)
        my_turtle.pendown()

drawTree(tree_depth, trunk_length)
turtle.done()
