"""
Frivillig, avansert: Endre programmet slik at annenhver diamant er fylt med svart og annenhver er
fylt med hvit. Start med å fylle med svart. Under er det et eksempel med 5 diamanter. Du kan også
prøve deg på mer enn to farger.
"""

import turtle

# Ber bruker om input for antall diamanter som skal tegnes
antall_diamanter = int(input("Hvor mange diamanter skal vi tegne? "))

# Setter en størrelse til å starte med og et increment jeg ønsker å bruke som utgangspunkt til å øke størrelsen
# på diamantene
base_size = 680
increment = 70

# Lager en definisjon som tegner diamantene
def draw_diamonds(current_size, colour):
    turtle.fillcolor(colour)
    turtle.begin_fill()
    turtle.pendown()
    for x in range(4):
        turtle.forward(current_size)
        turtle.left(90)
    turtle.end_fill()

# Tar turtle til startposisjon
turtle.penup()
turtle.goto(antall_diamanter*50 + 50, 0)
turtle.left(180)

# Setter opp en for loop for å tegne diamantene
for y in range(antall_diamanter):
    current_size = base_size - y*increment
    if y % 2 == 0:
        colour = "black"
    else:
        colour = "white"
    turtle.forward(50)
    turtle.right(45)
    turtle.pendown()
    draw_diamonds(current_size, colour)
    turtle.left(45)
    turtle.penup()

turtle.done()
