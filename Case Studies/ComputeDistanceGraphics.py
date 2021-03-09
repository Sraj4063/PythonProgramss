import turtle
print("make sure to have around atlaest 50 points difference between x1,x2 and y1,y2 for better visualization")
x1 = int(input())
y1 = int(input())

x2= int(input())
y2 = int(input())

distance = (((x1 - x2)**2) + ((y1 - y2)**2) ) ** 0.5
print("the distance between 2 points:"distance)

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write("point1")
turtle.goto(x2,y2)
turtle.write("point2")
turtle.pendown()

turtle.penup()
turtle.goto((x1+x2)/2, (y1+y2)/2)
turtle.write(distance)

turtle.done()
