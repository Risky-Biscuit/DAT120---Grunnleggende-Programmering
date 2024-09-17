"""
Funksjon med en parameter med returverdi: Skriv en funksjon som regner ut formelen f(x) =x*log2(x) og
returnerer resultatet.
"""

import math

def regn_ut_log(x):
    resultat = x * math.log2(x)
    return resultat


print(regn_ut_log(int(input("Velg en verdi for x: "))))
