"""
Et program som utfører Newton-Raphsons metode for å finne røttene til en funksjon.
"""
import numpy as np
from math import exp

# Definer funksjonen vi ønsker å finne roten til
def f(x):
    return (x-1)**2 * exp(x) - 0.5

# Definer derivatet av funksjonen
def df(x):
    return exp(x) * (x-1) * (x+1)

# Beregn endringen i x
def delta_x(x):
    return f(x) / df(x)

# Sett nøyaktighetsgrensen
noyaktighet = 0.000001

# Funksjon for å finne roten ved bruk av Newton-Raphsons metode
def newton_raphson(startverdi):
    c = startverdi
    while abs(delta_x(c)) > noyaktighet:
        c = c - delta_x(c)
    return round(c, 6)

# Finn numeriske tilnærminger for de tre røttene
startverdier = [-3, 0, 1.5]
rotter = [newton_raphson(start) for start in startverdier]

# Skriv ut løsningene
for i, rot in enumerate(rotter):
    print(f"Løsningen med startverdi {startverdier[i]} er {rot}")
