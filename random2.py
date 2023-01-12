import turtle
turtle.speed(10)
n = 15
pen = turtle.Turtle()
turtle.bgcolor('black')
for i in range(n):
    pen.pencolor('white')
    pen.forward(i * 10)
    pen.right(144)

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
turtle.bgcolor('black')
for x in range(360):
    pen.pencolor(colors[x%6])
    pen.width(x//100 + 1)
    pen.forward(x)
    pen.right(59)
turtle.done()