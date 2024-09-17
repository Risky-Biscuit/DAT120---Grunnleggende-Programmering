"""
Program for å finne fakultetet av et tall
"""
from unittest import skipIf

tall = int(input("Skriv inn tallet du vil ha fakultetet av: "))
while tall < 0:
    print("Fakultetet av negative tall finnes ikke.")
    tall = int(input("Skriv inn tallet du vil ha fakultetet av: "))
resultat = 1
for i in range(1, tall+1):
    resultat = resultat * i
    print(i, resultat)
print("Resultatet ble: ", resultat)
