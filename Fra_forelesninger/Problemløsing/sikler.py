"""
Lager sirkler helt til den har gått 360 grader
"""

import turtle

turtle.speed(11)

SIRKEL_STORRELSE = 100

VINKEL = 5

naaverende_vinkel = 0

MAKS_VINKEL = 360

while naaverende_vinkel < MAKS_VINKEL:
    turtle.circle(SIRKEL_STORRELSE)
    turtle.right(VINKEL)
    naaverende_vinkel += VINKEL
turtle.done()