"""
Bruk av ferdigdefinerte funksjoner / repetisjon: I turtle graphics oppgir man hvor mye man
skal rotere med i grader. I matematikk-bibliotekene til Python bruker man radianer for å
oppgi vinkler. Du kan bruke funksjonene math.radians(grader) og math.degrees(radianer) for
å konvertere. Du må importere math-biblioteket for å få tilgang til disse to funksjonene.
Skriv et program som bruker Turtle Graphics til å tegne en rettvinklet trekant der bruker
oppgir lengde på linja langs x-aksen (n) og vinkel mellom den linja og hypotenus. Scriptet ditt
skal regne ut lengdene til de to andre linjene. Formlene for lengden til de to andre linjene blir
da hypotenus = n/cos(vinkel) og motsatt = n*tan(vinkel).
"""

import math
import turtle

# Først en funksjon som ber om lengden på kateten og vinkelen mellom denne og hypotenusen som jeg behøver
def be_om_verdier():
    lengde_katet = int(input("Hvor mange piksler lang ønsker du at kateten skal være? "))
    vinkel = int(input("Hvor mange grader ønsker du at vinkelen mellom horisontal katet og hypotenus skal være? "))
    vinkel_i_radianer = math.radians(vinkel)        # Gjør om fra grader til radianer
    return lengde_katet, vinkel, vinkel_i_radianer  # Gjør verdiene globale


lengde_katet, vinkel, vinkel_i_radianer = be_om_verdier()   # Fanger opp verdiene'


def regn_ut_trekant(lengde_katet, vinkel_i_radianer):
    lengde_hypotenus = lengde_katet/math.cos(vinkel_i_radianer) # Finner lengden av hypotenusen
    lengde_katet_2 = lengde_katet*math.tan(vinkel_i_radianer)   # Finner lengden av den andre kateten
    return lengde_hypotenus, lengde_katet_2                     # Gjør verdiene globale


# Funksjon for å tegne trekanten
def tegn_trekant(lengde_katet, vinkel, lengde_hypotenus, lengde_katet_2):
    turtle.left(180)
    turtle.pendown()
    turtle.forward(lengde_katet)
    turtle.left(180)
    turtle.left(vinkel)
    turtle.forward(lengde_hypotenus)
    turtle.right(180)
    turtle.left(180-90-vinkel)
    turtle.forward(lengde_katet_2)
    turtle.done()


lengde_hypotenus, lengde_katet_2 = regn_ut_trekant(lengde_katet, vinkel_i_radianer) # Fanger opp verdiene

regn_ut_trekant(lengde_katet, vinkel_i_radianer)                                    # Kaller på funksjonen som regner ut sidene

tegn_trekant(lengde_katet, vinkel, lengde_hypotenus, lengde_katet_2)                # Kaller på funksjonen som tegner trekanten
