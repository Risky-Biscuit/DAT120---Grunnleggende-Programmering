"""
Erlend (foreleser) har laget denne filen for å vise eksempler på bruk av lister, tupler og numpy arrays.
"""

# Lager ei ny liste med elementene 6, 3, 7, 5 og 4
liste = [6, 3, 7, 5, 4]

# Skriver ut det første elementet i lista. Python indekser starter å telle fra 0.
print(liste[0])

# Skriver ut det tredje elementet i lista
print(liste[2])

# Skriver ut det femte elementet i lista
print(liste[4])

# Du kan bruke negative indekser for å telle fra slutten av lista.
# Skriver ut det siste elementet i lista
print(liste[-1])

# Skriver ut det nest siste elementet i lista
print(liste[-2])

# Får en IndexError hvis du bruker en indeks som er utenfor lista
print(liste[5])
print(liste[-6])

# Skriver ut lengden til lista
print(len(liste))

# Kan lage ei liste med elementer av ulike typer
liste2 = [7, 4, 3, "test", 6.7, 7, "to"]

# Skriver ut lengde til liste 2
print(len(liste2))

# Kan tilordne verdier til enkeltelementer i ei liste, her
# settes det tredje elementet av liste2 lik 11
liste2[2] = 11

# Lister kan inneholde andre lister som elementer
liste2[1] = [1, 2, 3]

# Skriver ut lista som er element i liste2
print(liste2[1])

# Starter i liste 2. Henter ut det andr elementet i lista. Det elementet
# Henter er selv ei liste. Henter ut det andre elementet i denne indre
# lista.
print(liste2[1][1])

# Legger til elementet 23 til slutten av liste 2
liste2.append(23)

# Skriver ut alle elementene i lista "liste"
for i in range(len(liste)):
    print(liste[i])

# Kan gå gjennom ei liste på denne måten med en for-løkke
for element in liste:
    print(element)

# Kan slå sammen to lister med + operatoren
sammenslaatte_lister = liste + liste2
print(sammenslaatte_lister)

# Kan bruke * operatoren til å repetere ei liste, i dette
# tilfellet 5 ganger.
kort_liste = [0, 1]
repeterende_liste = kort_liste * 5
print(repeterende_liste)

# Henter ut en del av ei liste. I dette tilfellet alle elementer
# fra og med indeks 2, til men ikke med indeks 6. Dette kalles
# list slicing på engelsk.
print(liste2[2:6])
test = liste2[2:6]
liste2[2] = 13

# Starter på starten og går til men ikke med indeks 5
print(liste2[:5])

# Starter på indeks 5 og går til slutten av lista
liste2[5:]

# Starter på indeks 1, går til men ikke med indeks 6, og tar med bare
# annenhvert element (steglengde 2)
liste2[1:6:2]

# Kan bruke in-operatoren for å sjekke om et element er med i ei liste
print(5 in liste)
print(1 in liste)

# Bruk av in-operatoren i en if-setning
if 5 in liste:
    print("5 er med i lista")

# Henter ut indeksen til første forekomst av elementet 5
print(liste.index(5))

# Henter ut indeksen til første forekomst av elementet 7
liste2.index(7)

# Setter inn elementet 8 på indeks 2, forskyver alle elementer på indeks 2 eller høyere
# ett hakk utover i lista.
liste.insert(2, 8)

# Sorterer lista
liste.sort()

# Kan bare sortere lister hvor alle elementene er sammenliknbare. Får ellers
# en TypeError
liste2.sort()

# Fjerner første forekomst av elementet 5
liste.remove(5)

# Fjerner første forekomst av elementet 7
liste2.remove(7)

# Reverserer lista slik at den nå er i motsatt rekkefølge
liste.reverse()

# Fjerner elementet på indeks 2
del liste[2]

# Lager ei ny tom liste
ny_liste = list()

# Legger til elementer i lista
ny_liste.append(12)
ny_liste.append(23)

# Finner minste element i lista
print(min(liste))

# Finner største element i lista
print(max(liste))

# Elementene må være sammenliknbare som for sortering
print(max(liste2))

# Kan bruke enumerate-funksjonen for å få ut både indeks og element
# i ei liste på denne måten
for index, element in enumerate(liste):
    print(f"Elementet på posisjon {index} er {element}")

# Lager en streng. Strenger likner ei liste med tegn
strengen = "Strenger er lister av tegn"

# Henter ut tegnet på tredje posisjon i strengen
print(strengen[2])

# Henter ut nest siste tegn i strengen
print(strengen[-2])

# Skriver ut hvert tegn i strengen
for tegn in strengen:
    print(tegn)

# Skriver ut lengden til strengen (antall tegn den består av)
print(len(strengen))

# Kan hente ut deler av en streng som for lister
print(strengen[3:10])

# Kan ikke tilordne verdier til enkelttegn i en streng. Strenger
# er uforanderlige
strengen[5] = "g"

# Kan bruke split metoden for å splitte en streng basert på et tegn.
# Her henter den ut de enkelte ordene med å splitte strengen
# på åpenromstegnet. split returnerer ei liste av strenger.
ordene = strengen.split(" ")

# Skriver ut hvert ord
for element in ordene:
    print(element)

# Importerer datetime
import datetime

# Lager et datetime objekt for nåværende tidspunkt
naa = datetime.datetime.now()
print(naa)

# Lager et datetime objekt for tidspunktet 5. mars 2024 klokka 12:15:00.
# Rekkefølgen er år, måned, dag, timer, minutter, sekunder
et_tidspunkt = datetime.datetime(2024, 3, 5, 12, 15, 00)

# Kan bruke navngitte parametere når man lager datetime objekter
et_tidspunkt_til = datetime.datetime(year=2023, month=9, day=23)

# Kan sammenlikne datetime objekter
print(et_tidspunkt < et_tidspunkt_til)
print(et_tidspunkt > et_tidspunkt_til)

# Henter ut komponentene
print(et_tidspunkt.year)
print(et_tidspunkt.month)
print(et_tidspunkt.day)
print(et_tidspunkt.hour)
print(et_tidspunkt.minute)
print(et_tidspunkt.second)
