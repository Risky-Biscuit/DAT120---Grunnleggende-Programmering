"""
Funksjon med en parameter uten returverdi: Start med koden fra øving 2 for oppgaven der
du skal tegne en sekskant med Turtle Graphics. Skriv om denne koden til en funksjon.
Funksjonen skal ta inn lengden på sidene til sekskanten som en parameter.
"""

import turtle


def tegn_sekskant(sidelengde):
    turtle.color("blue")                                        # Funksjonen tegner en sekskant med gitt sidelengde
    turtle.pensize(2)
    turtle.speed(3)


    for i in range(6):
        turtle.forward(sidelengde)
        turtle.left(60)

    turtle.done()


lengde = float(input("Hvor lange sider ønsker du? "))           # Kall funksjonen med brukerens input

tegn_sekskant(lengde)                                           # Kall funksjonen med brukerens input
