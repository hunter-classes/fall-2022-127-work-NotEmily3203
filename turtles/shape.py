import turtle

wn = turtle.Screen()

crush = turtle.Turtle()

crush.forward(50)
crush.left(90)
crush.forward(50)
crush.left(90)
crush.forward(50)
crush.left(90)
crush.forward(50)
crush.left(90)

#  create second turtle named squirt and draw a triangle

squirt = turtle.Turtle()

squirt.goto(100,100)

squirt.color("light blue")


squirt.forward(30)
squirt.left(120)
squirt.forward(30)
squirt.left(120)
squirt.forward(30)

wn.exitonclick()
wn.mainloop()