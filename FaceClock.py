import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)
tess.shape("turtle")
tess.stamp()

for i in range(12):
    tess.penup()
    tess.forward(150)
    tess.pendown()
    tess.forward(30)
    tess.penup()
    tess.forward(20)
    tess.stamp()
    tess.setpos(0,0)
    tess.left(360/12)
    
tess.hideturtle()

    
   
