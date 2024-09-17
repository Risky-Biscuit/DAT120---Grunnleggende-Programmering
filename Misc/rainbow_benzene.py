"""
Turtle draws a Rainbow Benzene
"""

import turtle
colours = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.speed(10)
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colours[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)
turtle.done()
