"""
Dette programmet viser hvordan funksjoner kan endre på variabler som blir sendt inn som argumenter.
"""

def endrer_tall(tallet):
    tallet += 5
    return tallet

def endrer_liste(listen):
    listen.append(6)
    return listen

def feil_default_verdi(verdi, liste=[]):
    liste.append(verdi)
    return liste

print(endrer_tall(5))
print(endrer_tall(10))      # Når vi kaller funksjonen endrer_tall igjen er den UAVHENGIG av forrige kall
print(endrer_liste([1, 2, 3, 4, 5]))
print(endrer_liste([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))    # Når vi kaller funksjonen endrer_liste igjen er den UAVHENGIG av forrige kall
print(feil_default_verdi(1))
print(feil_default_verdi(2))    # Når vi kaller funksjonen feil_default_verdi igjen er den AVGENGIG av forrige kall


def riktig_default_verdi(verdi, liste=None):
    if liste is None:
        liste = []
    liste.append(verdi)
    return liste

print(riktig_default_verdi(1))
print(riktig_default_verdi(2))  # Når vi kaller funksjonen riktig_default_verdi igjen er den UAVHENGIG av forrige kall