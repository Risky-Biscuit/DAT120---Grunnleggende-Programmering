"""
Program som tegner en sekskant ved hjelp av en funksjon
"""

import turtle


def sekskant_sider(sidelengde):
    tall = float(input(sidelengde))
    return tall

lengde = sekskant_sider("Hvor lange sider ønsker du? ") # Ber om lengde på sidene

# Sett opp turtle
turtle.color("blue")                                    # Setter farge til blå
turtle.pensize(2)                                       # Setter størrelse på pennen til 2
turtle.speed(3)                                         # Setter farten på pennen til 3


for i in range(6):                                      # Setter opp en for loop som tegner sekskanten
    turtle.forward(lengde)                              # Gå n piksler frem
    turtle.left(60)                                     # Roter 60 grader til høyre
turtle.done()
