import turtle 
turtle.Screen().bgcolor("lightgreen")
turtle.Screen().setup(300, 400)
polygon = turtle.Turtle()
num_sides = int(input("enter the number of sides"))
side_length = 70
angle = 360.0 / num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.left(angle)
turtle.done()