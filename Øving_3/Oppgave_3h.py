"""
Frivillig, mengdetrening: Skriv en funksjon som regner ut den euklidske avstanden fra origo
(punktet med koordinatene 0, 0) og til et punkt. Funksjonen skal ta x- og y-koordinatene til
punktet som parametere. Funksjonen skal returnere avstanden. Formelen for avstanden er
𝑎𝑣𝑠𝑡𝑎𝑛𝑑 = √𝑥2 + 𝑦2
"""

import math

print("Vi skal regne ut den euklidske avstanden til et punkt fra origo")

x = float(input("Hva er x-koordinatene? "))
y = float(input("Hva er y-koordinatene? "))

def absolutt_vektor(x,y):
    resultat = math.sqrt(x**2 + y**2)
    return resultat

print(f"Den euklidske avstaden til punktet fra origo er {absolutt_vektor(x, y)}")
