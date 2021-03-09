import turtle

turtle.pensize(3) #set the thickness to 3 pixels
turtle.penup()
turtle.goto(-200,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(40,steps = 3) # a triangle
turtle.end_fill()

turtle.pensize(3) #set the thickness to 3 pixels
turtle.penup()
turtle.goto(-100,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color("green")
turtle.circle(40,steps = 4) # a square
turtle.end_fill()

turtle.pensize(3) #set the thickness to 3 pixels
turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color("brown")
turtle.circle(40,steps = 5) # a pentagon
turtle.end_fill()

turtle.pensize(3) #set the thickness to 3 pixels
turtle.penup()
turtle.goto(100,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.circle(40,steps = 6) # a hexagon
turtle.end_fill()

turtle.pensize(3) #set the thickness to 3 pixels
turtle.penup()
turtle.goto(200,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color("yellow")
turtle.circle(40) # a cirlce
turtle.end_fill()

turtle.color("black")
turtle.penup()
turtle.goto(-100,50)
turtle.pendown()
turtle.write("cool colorful shapes",font = ("Arial",18, "bold"))
turtle.hideturtle()
             
turtle.done()
