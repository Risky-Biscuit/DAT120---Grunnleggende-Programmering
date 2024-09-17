"""
Dette er en gjennomgang av alt man kan gjøre med lister
"""

liste = [0, 6, 4, 2, 9, 11]

print(liste)

# Python teller fra null, så element 2 er egentlig element nr 3
print(liste[2])

# Negative indekser teller bakover bakfra
print(liste[-1])

# Vi kan sjekke lengden av listen ved hjelp av len funksjonen
listelengde = len(liste)
print(f"Listen er {listelengde} elementer lang.")

# Listen kan inneholde flere forskjellige typer verdier
test_variabel = 3
liste2 = [1, 1.2, "test", test_variabel]
print(liste2)

# Vi kan endre det som er i listen
liste2[1] = 11
print(liste2)

# Vi kan til og med lagre en liste inni en liste
liste2[2] = [1, 2, 3]
print(liste2)

# Vi kan hente ut ting fra lista inni lista
print(liste2[2][1])

# Vi kan legge til elementer i lister
liste2.append(23) # Slik blir tallet 23 lagt til på slutten av listen
print(liste2)

# Vi kan bruke lengden på lista i andre funksjoner også
for i in range(len(liste)):
    print(liste[i])

# Vi kan gjøre det samme på en annen måte også
for element in liste:
    print(element)

# Vi kan også bruke operatorer på listene
liste3 = liste + liste2
print(liste3)

# Lista kan mangedobles ved hjelp av multiplisering
kort_liste = [0, 1, 4]
liste4 = kort_liste*5
print(f"Kort liste * 5 blir {liste4}")

# Vi kan splitte lister. Dvs hente ut en del av listen. Her henter vi fra indeks 2 til, men IKKE med, indeks 6
print(liste2[2:6])
# Om vi lar være å oppgi første tall så starter vi på starten av lista
print(liste2[:4])
# Det samme kan vi gjøre motsatt for å gå til slutten av lista
print(liste2[3:])

# Vi kan også spesifisere steglengde - her starter vi på 1, går til men ikke med 4 med steglengde 2
print(liste[1:4:2])

# Vi kan også sjekke om noe er med i en liste. Dette vil i utgangspunktet bli registrert som True eller False
# Men vi kan komme oss rundt dette
if 6 in liste:
    print("6 er med i lista.")
else:
    print("6 er ikke med i lista.")

# Vi kan finne ut hvor i lista noe er
print(f"Tallet 6 er element nummer {liste.index(6)} i lista.")

# Vi kan også legge til ting i lista. Her settes elementet 8 i indeks 2
liste.insert(2, 8)
# Dette er ikke likt som å overskrive et element i lista ved å gjøre
liste[2] = 8
# Ved å bruke liste.insert() så forskyves alt som er bak der vi legger inn noe nytt én plass bak.
# Så lista blir forlenget med et element i stedet for at et element blir byttet ut med et annet.

# Vi kan sortere lista så lenge alle elementene i lista kan sammenlignes med hverandre
liste.sort()
print(liste)

# Om vi forøskte å skrive print(liste2.sort()) så ville vi fått en TypeError fordi ikke alle elementene
# sammenlignbare med hverandre

# Vi kan fjerne elementer fra lista. Her fjernes elementet 6 fra liste
liste.remove(6)
print(liste)
# Dersom tallet du forsøker å fjerne så er det kun den første forekomsten av tallet som blir fjernet.

# Vi kan også fjerne basert på indeks. Her fjernes hva enn som er på indeks 2
del liste[2]

# Vi kan også flippe om lista slik at den går andre vei
liste.reverse()
print(liste)

# Om vi skal lese inn verdier fra en fil og legge inn i en liste så starter vi med en tom liste
# list() er en funksjon som lager en tom liste
ny_liste = list()
ny_liste.append(12)
ny_liste.append(23)
print(ny_liste)

# Vi kan bruke min og max for å få ut det minste og største elementet. Dette gjelder igjen kun når elementene
# er sammenlignbare.
print(f"Minste elementet på den nye listen er {min(ny_liste)}")
print(f"Største elementet på den nye listen er {max(ny_liste)}")

# Vi kan hente ut på element og indeks ved å bruke enumerate
for indeks, element in enumerate(liste):
    print(f"Elementet på posisjon {indeks} er {element}")

