import turtle

wn = turtle.Screen()
pirate = turtle.Turtle()

for i in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    pirate.left(i)
    pirate.forward(100)

print("The current heading is",pirate.heading())

wn.exitonclick()
wn.mainloop()