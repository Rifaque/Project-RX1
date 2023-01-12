import turtle as r
import colorsys as cs
r.setup(800, 800)
r.speed(0)
r.width(2)
r.bgcolor("black")
for j in range (25):
    for i in range (15):
        r.color(cs.hsv_to_rgb(i/15,j/25,1))
        r.right(90)
        r.circle(200-j*4,90)
        r.left(90)
        r.circle(200-j*4,90)
        r.right(180)
        r.circle(50,24)
r.hidertle()
r.done()