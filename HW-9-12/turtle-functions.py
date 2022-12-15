import turtle

wn = turtle.Screen()

def hexagon(t,x,y,w,color,sidelen):
  """ 
  Draw a hexagon using the turtle passed into t
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
  for i in range(6):
    t.forward(sidelen)
    t.left(60)

def ngon(t, numsides,x,y,color,width, sidelen):
  """ 
  Draw any shape using the turtle passed into t
  Parameters: 
  t = Turtle
  numsides = amount of sides
  x,y = coordinate points
  color = color of the line
  width = width of line
  sidelen = length of each side
  """
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.color(color)
  t.width(width)
  x=360/numsides
  y=0
  while y != 360:
    y = y+x
    t.left(x)
    t.forward(sidelen)

squirt = turtle.Turtle()
crush = turtle.Turtle()

hexagon(squirt, 10, -10, 20, "orange",80)
ngon(squirt, 7, -10, 10, "green",30, 100)

wn.exitonclick()
wn.mainloop()