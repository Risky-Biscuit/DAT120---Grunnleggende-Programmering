"""
Frivillig, avansert: Lag en funksjon som bruker funksjonen fra deloppgave b til å tegne n
sekskanter under hverandre tilsvarende øving 2 oppgave k)
"""
import turtle


def tegn_sekskant(sidelengde, antall):
    turtle.color("blue")                                        # Funksjonen tegner en sekskant med gitt sidelengde
    turtle.pensize(2)
    turtle.speed(3)

    if antall == 1:
        for _ in range(6):
            turtle.pendown()  # Sett ned pennen
            turtle.forward(80)  # Gå frem 80 piksler
            turtle.right(60)  # Roter 60 grader til høyre

    if antall > 1:
        turtle.pendown()  # Sett ned pennen
        for _ in range(6):
            turtle.forward(80)  # Gå frem 80 piksler
            turtle.right(60)  # Roter 60 grader til høyre
        turtle.penup()
        turtle.right(120)
        turtle.forward(80)
        turtle.left(60)
        turtle.forward(80)
        turtle.left(60)
        turtle.forward(80)
        turtle.pendown()
        for x in range(antall - 1):
            turtle.right(60)
            turtle.forward(80)
            turtle.right(60)
            turtle.forward(80)
            turtle.right(60)
            turtle.forward(80)
            turtle.right(60)
            turtle.forward(80)
            turtle.right(60)
            turtle.forward(80)
            turtle.right(60)
            turtle.forward(80)
            turtle.right(60)
            turtle.forward(80)
            turtle.right(60)
            turtle.forward(80)
            turtle.left(120)

    turtle.done()


lengde = 50         # Sett lengde til 50

sekskanter = int(input("Hvor mange figurer ønsker du? "))

# Flytt skilpadden opp på skjermen for å få mer plass
turtle.penup()      # løft pennen
turtle.left(90)     # Roter 90 grader til venstre
turtle.forward(300) # Går frem 300 piksler
turtle.right(90)    # Roter 90 grader til høyre

tegn_sekskant(lengde, sekskanter)                                           # Kall funksjonen med brukerens input
