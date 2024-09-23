"""
Tegner en stjerne
"""

import turtle

LENGDE = 100
VINKEL = 170

turtle.speed(7)
turtle.fillcolor("orange")
turtle.begin_fill()
turtle.forward(LENGDE)
for i in range(36):
    turtle.right(VINKEL)
    turtle.forward(LENGDE*2)
turtle.end_fill()
turtle.done()
