"""
Frivillig, mengdetrening: Skriv en funksjon som bruker funksjonen fra forrige deloppgave til å
regne ut avstanden mellom to punkter. Funksjonen skal ta inn x- og y- koordinatene til de to
punktene. Funksjonen skal regne ut hva den skal sende inn til funksjonen i forrige
deloppgave gjennom å flytte begge punktene slik at det første punktet ligger i origo, altså
skal den bruke koordinatene x2-x1 og y2-y1. Her er x1 x-koordinaten til det første punktet og
x2 er x-koordinaten til det andre punktet, og tilsvarende for y-koordinatene
"""

import math

x1 = 2
y1 = 5

x2 = 5
y2 = 9

def absolutt_vektor(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    resultat = math.sqrt(x**2 + y**2)
    return resultat

print(f"Den euklidske avstanden mellom de to punktene er {absolutt_vektor(x1, y1, x2, y2)}")
