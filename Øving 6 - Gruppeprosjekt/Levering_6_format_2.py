import datetime
import matplotlib.pyplot as plt
import numpy as np

dataliste = list()

with open("data/trykk_og_temperaturlogg_rune_time.csv.txt", "r") as fila:
    for lines in fila:                              #For hver linje i fila
        verdi = lines.strip().split(";")            #Fjern whitespace og split ord med ;
        for ord in verdi:                           #For ord i verdi
            dataliste.append(ord)                   #Legg til ordet/datapunktet i lista

def listedeling(listenavn, startverdi, stegverdi):             #Funksjon som brukes til å dele opp den store liste i mindre lister
    listenavn = dataliste[startverdi : 60495 : stegverdi]   #Funksjonen tar en startverdi som er første gang et datapunkt dukker opp. Sluttverdi og stegverdi er basert på fila
    return listenavn

datoliste3 = list()
temperaturliste3 = list()
lufttrykk3 = list()
absoluttrykk = list()
datolistetrykk = list()

datoliste3 = listedeling(datoliste3, 5, 60495, 5)
temperaturliste3 = listedeling(temperaturliste3, 9, 60495, 5)
lufttrykk3 = listedeling(lufttrykk3, 7, 60495, 5) #30 steg
absoluttrykk = listedeling(absoluttrykk, 8, 60495, 5)
datolistetrykk = listedeling(datolistetrykk, 5, 60495, 30)

print(lufttrykk3)

temperaturliste4 = list()
lufttrykk4 = list()
absoluttrykk2 = list()

for trykk in absoluttrykk:                       #Konverterer kommatallene i temperaturliste 1 til flyttall i temperaturliste 2
    absoluttrykk2.append(float(trykk.replace(",", ".")))

for temperatur in temperaturliste3:            #Konverterer kommatallene i temperaturliste 1 til flyttall i temperaturliste 2
    temperaturliste4.append(float(temperatur.replace(",", ".")))

for trykk in lufttrykk3:            #Konverterer kommatallene i temperaturliste 1 til flyttall i temperaturliste 2
    if trykk == "":
        continue
    else:
        lufttrykk4.append(float(trykk.replace(",", ".")))
        trykket = float(trykk.replace(",", "."))

format = "%m.%d.%Y %H:%M"
datolistedatetime2 = list()
datolistedatetimetrykk = list()

for dato in datoliste3:                                     #Konverterer verdiene i datoliste1 til datetime-objekter
    datolistedatetime2.append(datetime.datetime.strptime(dato, format))
for dato in datolistetrykk:                                 #Konverterer verdiene i datoliste1 til datetime-objekter
    datolistedatetimetrykk.append(datetime.datetime.strptime(dato, format))


temperaturarray2 = np.array(temperaturliste4)                 #Lager arrays av de forskjellige datapunktene for plotting
datoarray2 = np.array(datolistedatetime2)
abstrykkarray = np.array(absoluttrykk2)
lufttrykkarray2 = np.array(lufttrykk4)
datotrykkarray = np.array(datolistedatetimetrykk)
print(lufttrykk4)

plt.subplot(3, 1, 1)
plt.plot(array1, array2, color = "pink")
plt.subplot(3, 1, 2)
plt.plot(array1, array3)
plt.plot(array5, array4)
plt.show()