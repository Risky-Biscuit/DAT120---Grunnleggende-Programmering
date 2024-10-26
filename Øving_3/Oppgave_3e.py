"""
Script som bruker egendefinert funksjon: Skriv et script som leser inn to tall m og n. Scriptet
skal bruke funksjonen fra oppgave d) til å regne ut m*log(m) + n*log(n) og skrive ut
resultatet
"""

import math

print("Vi skal regne ut m*math.log2(m) + n*math.log(n)")
m = int(input("Gi 'm' en tallverdi: "))
n = int(input("Gi 'n' en tallverdi: "))

def regn_ut_log(m, n):
    resultat = m * math.log(m) + n * math.log(n)
    return resultat


print(f"Resultatet av m * math.log(m) + n * math.log(n) er {regn_ut_log(m, n):.4f}")
