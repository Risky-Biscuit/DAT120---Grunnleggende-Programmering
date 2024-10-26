"""
Script som bruker egendefinert funksjon: Bruk funksjonen fra oppgave b til å tegne fire
sekskanter med ulik størrelse på ulike steder, velg selv hvor de tegnes og hvor store de skal
være
"""

import turtle

def tegn_sekskant(sidelengde):
    # Funksjonen tegner en sekskant med gitt sidelengde
    for i in range(6):
        turtle.forward(sidelengde)
        turtle.left(60)


# Funksjon for å flytte skilpadden til en ny posisjon uten å tegne
def flytt_til(x, y):
    turtle.penup()          # Løft pennen opp
    turtle.goto(x, y)       # Flytt til (x, y)-posisjonen
    turtle.pendown()        # Sett pennen ned igjen


# Sett opp skilpadden
turtle.color("blue")
turtle.pensize(2)
turtle.speed(3)

# Tegn fire sekskanter på ulike steder med ulik størrelse
flytt_til(-100, 100)     # Flytt til øvre venstre hjørne
tegn_sekskant(50)           # Tegn en sekskant med sidelengde 50

flytt_til(100, 100)   # Flytt til øvre høyre hjørne
tegn_sekskant(70)           # Tegn en sekskant med sidelengde 70

flytt_til(-100, -100)       # Flytt til nedre venstre hjørne
tegn_sekskant(90)           # Tegn en sekskant med sidelengde 90

flytt_til(100, -100)     # Flytt til nedre høyre hjørne
tegn_sekskant(120)          # Tegn en sekskant med sidelengde 120

# Fullfør tegningen
turtle.done()
