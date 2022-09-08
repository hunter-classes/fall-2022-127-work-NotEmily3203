import turtle

wn = turtle.Screen()

def square(t,x,y,w,color,sidelen):
  #use triple string to return text
  """ 
  Draw a square using the turtle passed into t
  Parameters: 
  t = Turtle
  x,y = coordinate points
  w = width
  color = color of the line
  sidelen = length of each side
  """
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.color(color)
  t.width(w)
  for i in range(4):
    t.forward(sidelen)
    t.left(90)

def triangle(t,x,y,w,color,sidelen):
  """ 
  Draw a triangle using the turtle passed into t
  Parameters: 
  t = Turtle
  x,y = coordinate points
  w = width
  color = color of the line
  sidelen = length of each side
  """
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.color(color)
  t.width(w)
  for i in range(3):
    t.forward(30)
    t.left(120)

def ngon(t, sides, sidelen):
  """ 
  Draw any shape using the turtle passed into t
  Parameters: 
  t = Turtle
  sides = amount of sides
  sidelen = length of each side
  """
  x=360/sides
  y=0
  while y != 360:
    y = y+x
    t.left(x)
    t.forward(sidelen)

squirt = turtle.Turtle()
crush = turtle.Turtle()

square(crush, 10, 10, 10, "pink",50)
triangle(crush, -10, -10, 10, "light blue",20)
ngon(squirt, 6, 100)

wn.exitonclick()
wn.mainloop()