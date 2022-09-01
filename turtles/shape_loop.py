import turtle

wn = turtle.Screen()

crush = turtle.Turtle()
squirt = turtle.Turtle()

for i in range(4):
  crush.forward(50)
  crush.left(90)

squirt.goto(100,100)
squirt.color("light blue")

for i in range(3):
  squirt.forward(30)
  squirt.left(120)

wn.exitonclick()
wn.mainloop()