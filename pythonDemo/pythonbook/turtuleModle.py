import turtle

x1, y1 = input("please enter x1 and y1 for point 1:")
x2, y2 = input("please enter x2 and y2 for point 2:")

distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("point 1")
turtle.goto(x2, y2)
turtle.write("point 2")

turtle.penup()
turtle.goto((x1+x2)/2, (y1+y2)/2)
turtle.write(distance)
turtle.done()
