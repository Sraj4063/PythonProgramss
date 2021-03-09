import turtle
import math

radius = eval(input("enter the radius of the circle"))
area = radius * radius * math.pi
print("Area of the circle :", area)

turtle.penup()
turtle.goto(radius,0)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(radius,radius)
turtle.write(format(area,"10.2f"))
turtle.done()
