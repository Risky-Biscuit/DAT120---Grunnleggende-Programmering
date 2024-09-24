"""
Erlend (foreleser) har laget denne filen for å vise eksempler på bruk av lister, tupler og numpy arrays.
"""

ytre_liste = list()

ytre_liste.append([1, 3, 5])

ytre_liste.append([2, 4, 6])

ytre_liste.append([5, 4, 3])

print(ytre_liste)

print(ytre_liste[0])

print(ytre_liste[0][1])

print(ytre_liste[0][4])

ytre_liste[1].append(8)

print(ytre_liste[1][3])

print(ytre_liste[0][3])

lengde = 7

bredde = 6

lengde = lengde + 5

liste = [1, 2, 3, 4, 5]

liste2 = liste

liste.append(6)

print(liste2)


def endrer_tall(tallet):
    tallet += 5
    return tallet


def endrer_liste(liste):
    liste.append(6)
    return liste


# Aldri bruk et foranderlig objekt som
# default verdi
def feil_default_verdi(verdi, liste=[]):
    liste.append(verdi)
    return liste


print(endrer_tall(bredde))

print(endrer_liste(liste))

print(feil_default_verdi(3))

print(feil_default_verdi(7))

print(feil_default_verdi(8))


# Aldri bruk et foranderlig objekt som
# default verdi
def feil_default_verdi(verdi, liste=None):
    if liste is None:
        liste = list()
    liste.append(verdi)
    return liste


print(feil_default_verdi(8))

print(feil_default_verdi(6))

print(feil_default_verdi(3))

print(feil_default_verdi(3, liste))

print(feil_default_verdi(6))

print(feil_default_verdi(3))

liste3 = list(liste)

liste.append(4)

liste4 = liste[:]

liste4.append(13)

tuppel = (4, 5, 6)

print(tuppel)

for i in tuppel:
    print(i)

print(tuppel[1])

# Kan ikke tilordne til elementene i et tuppel
# tuppel[1] = 7

# Kan ikke appende til et tuppel
# tuppel.append(56)

tuppel2 = tuple(liste2)
print(tuppel2)

import numpy as np

array1 = np.zeros(10)

print(array1[5])

array1[5] = 5.4

# Kan ikke tilordne en streng som et element i en vanlig numpy
# array (som er en numpy array av flyttall)
# array1[6] = "test"

array2 = np.arange(7)
print(array2)

for i in range(1, 8, 2):
    print(i)

for i in range(1, 8, 0.5):
    print(i)

array3 = np.arange(1, 8, 0.5)

print(array3)

for i in np.arange(1, 5, 0.1):
    print(i)

array4 = np.linspace(1, 10, 4)

print(np.linspace(1, 10, 6))

print(np.array(liste))

array5 = np.array(liste)

array5[7] = 5.7

array5[7] = 7.8

array5[7] = 9

print(list(array3))

flerdimensjonal_array = np.zeros((3, 4))

print(flerdimensjonal_array)

flerdimensjonal_array[2, 3] = 5

print(flerdimensjonal_array)

flerdimensjonal_array[1, 0] = 3

print(flerdimensjonal_array)
