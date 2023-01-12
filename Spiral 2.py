#blue black spiral
import turtle
turtle.speed(0)
colors = ['blue', 'black', 'blue', 'black', 'blue', 'black']
t = turtle.Pen()
turtle.bgcolor('white')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.right(59)