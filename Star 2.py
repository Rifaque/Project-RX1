import turtle
turtle.speed(10)
n = 15
pen = turtle.Turtle()
turtle.bgcolor('black')
for i in range(n):
    pen.pencolor('white')
    pen.forward(i * 10)
    pen.right(144)
pen.hidertle()
turtle.done()