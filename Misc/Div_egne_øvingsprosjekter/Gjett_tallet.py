"""
Et enkelt spill jeg lager for å øve meg på noen grunnleggende konsepter i Python.
"""

from numpy.random import randint


tall = randint(0, 100)
antall_forsøk = 0

print("Du skal gjette et tall mellom 0 og 100.")

while True:
    gjettet_tall = int(input("Skriv inn tallet: "))
    if gjettet_tall == tall:
        antall_forsøk += 1
        print("Riktig!")
        print(f"Det tok deg {antall_forsøk} forsøk.")
        break
    elif gjettet_tall < tall:
        antall_forsøk += 1
        print("For lavt. Prøv igjen.")
    elif gjettet_tall > tall:
        antall_forsøk += 1
        print("For høyt. Prøv igjen.")
