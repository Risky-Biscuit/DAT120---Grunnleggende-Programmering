from punkt_properties import *


# Lager to strenger
streng = "En tekst"
streng2 = "En annen streng"

# Lager ei liste
liste = list()
liste.append(5)

print(liste)

# Konverterer den frste strengen til små bokstaver
print(streng.lower())

# Konverterer den andre strengen til små bokstaver
print(streng2.lower())

# Lager ei liste til
liste2 = list()
liste2.append(7)
liste2.append(12)

# Finner typen til ei liste og en int og ser at de begge starter med class
print(type(liste))
print(type(5))

# LAger et punkt og skriver ut egenskapene
punkt1 = Punkt()
print(punkt1.x_koordinat)
print(punkt1.y_koordinat)

print(punkt1)
liste.append(punkt1)
print(liste)

punkt2 = Punkt(5, 8)
print(punkt2)

punkt1.x_koordinat = 3
print(punkt1)
print(punkt2)

print(punkt2.avstand_fra_origo())
punkt2 = Punkt(3, 4)

print(punkt2.avstand_fra_origo())
print(punkt1.avstand_fra_origo())

# Må ha med en parameter til denne metoden
#punkt2.avstand()

print(punkt2.avstand(punkt1))
punkt1.x_koordinat = 3
print(punkt2.avstand(punkt1))
print(punkt1)
print(punkt2)

# Setter punkt3 til å referere til samme objekt som punkt1
punkt3 = punkt1
print(punkt3)
punkt3.y_koordinat = 2
print(punkt3)
print(punkt1)

# Eksempel på funksjon som modifiserer objektet: flytt_til_midten
flytt_til_midten(punkt1, punkt2)
print(punkt2)
print(punkt1)

# Lager nye punkter for å demonstrere rett linje klassen
punkt1 = Punkt(1, 1)
punkt2 = Punkt(4, 5)
punkt3 = Punkt(7, 5)
linje1 = RettLinje(punkt1, punkt2)
print(linje1)
print(linje1.lengde())

# Flytter et koordinat av et punkt go flytter dermed også linja som bruker
# dette punktet
punkt1.y_koordinat = 2
print(linje1)
print(linje1.lengde())

# Eksempel på bruk av funksjon som returnerer et punkt
punkt4 = skriv_inn_punkt()
print(punkt4)
punkt2 = Punkt(4, 5)

# Eksempel på bruk av properties r og theta
print(punkt2.r)
punkt2 = Punkt(3, 4)

print(punkt2.r)
print(punkt2.theta)

# Eksempel på tilordning av r gjennom r sin setter
punkt2 = Punkt(3, 3)
print(punkt2.r)
print(punkt2.theta)
punkt2.r = 9
print(punkt2.theta)
print(punkt2.r)
print(punkt2.x_koordinat)
print(punkt2.y_koordinat)

# Eksempel på bruk av x som property
punkt2 = Punkt(3, 4)
punkt2.x_koordinat = 8
print(punkt2)
# Får ValueError
punkt2.x_koordinat = -7
