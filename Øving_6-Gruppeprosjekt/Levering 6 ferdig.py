import datetime
import matplotlib.pyplot as plt
import numpy as np

dataliste1 = list()
dataliste2 = list()

with open("data/temperatur_trykk_met_samme_rune_time_datasett.csv.txt", "r") as fil1:
    for lines in fil1:                              #For hver linje i fil1
        verdi = lines.strip().split(";")            #Fjern whitespace og split ord med ;
        for ord in verdi:                           #For ord i verdi
            dataliste1.append(ord)                  #Legg til ordet/datapunktet i dataliste1

with open("data/trykk_og_temperaturlogg_rune_time.csv.txt", "r") as fil2:
    for lines in fil2:                              #For hver linje i fil2
        verdi = lines.strip().split(";")            #Fjern whitespace og split ord med ;
        for ord in verdi:                           #For ord i verdi
            dataliste2.append(ord)                  #Legg til ordet/datapunktet i dataliste2

def listedeling(listenavn, startverdi, sluttverdi, stegverdi, dataliste):      #Funksjon som brukast til å dela opp dei store listene i mindre lister
    listenavn = dataliste[startverdi : sluttverdi : stegverdi]
    return listenavn

datoliste1 = list()                                 #Lager ein del lister for data i dataliste1
temperaturliste1 = list()
lufttrykk1 = list()

datoliste2 = list()                                 #Lager ein del lister for data i dataliste2
temperaturliste3 = list()
lufttrykk3 = list()
absoluttrykk1 = list()
datolistetrykk = list()

datoliste1 = listedeling(datoliste1, 7, 365, 5, dataliste1)                     #Bruker listedelingfunksjonen til å å fylle opp listene
temperaturliste1 = listedeling(temperaturliste1, 8, 365, 5, dataliste1)
lufttrykk1 = listedeling(lufttrykk1, 9, 365, 5, dataliste1)

datoliste2 = listedeling(datoliste2, 5, 60495, 5, dataliste2)
temperaturliste3 = listedeling(temperaturliste3, 9, 60495, 5, dataliste2)
lufttrykk3 = listedeling(lufttrykk3, 7, 60495, 5, dataliste2)
absoluttrykk1 = listedeling(absoluttrykk1, 8, 60495, 5, dataliste2)
datolistetrykk = listedeling(datolistetrykk, 5, 60495, 30, dataliste2)

temperaturliste2 = list()                          #Lager fleire lister som skal innehalda listedata som vert konvertert til flyttal
lufttrykk2 = list()
temperaturliste4 = list()
lufttrykk4 = list()
absoluttrykk2 = list()

def konverterfloat(listenavn, listenavn2):         #Funksjon som konverterer listedata med komma som desimalseparator til flyttal
    for i in listenavn:
        listenavn2.append(float(i.replace(",", ".")))

konverterfloat(lufttrykk1, lufttrykk2)             #Konverterer temperaturer og trykkverdier til flyttal
konverterfloat(temperaturliste1, temperaturliste2)
konverterfloat(temperaturliste3, temperaturliste4)
konverterfloat(absoluttrykk1, absoluttrykk2)

for trykk in lufttrykk3:                           #Konverterer lufttrykkverdien frå fil 2 til flyttal
    if trykk == "":                                #Fordi fila ikkje inneheld eit datapunkt for kvar linje må denne behandlast annleis
        continue                                   #Dette er òg grunnen til at det er 3 datolister i staden for 2
    else:
        lufttrykk4.append(float(trykk.replace(",", ".")))
        trykket = float(trykk.replace(",", "."))

format1 = "%d.%m.%Y %H:%M"                         #Brukast til å beskriva datoformat i dei to filene
format2 = "%m.%d.%Y %H:%M"
datolistedatetime = list()
datolistedatetime2 = list()
datolistedatetimetrykk = list()

for dato in datoliste1:                               #Konverterer verdiene i datoliste1 til datetime-objekter i lista datolistedatetime
    datolistedatetime.append(datetime.datetime.strptime(dato, format1))
for dato in datoliste2:                               #Konverterer verdiene i datoliste2 til datetime-objekter i lista datolistedatetime2
    datolistedatetime2.append(datetime.datetime.strptime(dato, format2))
for dato in datolistetrykk:                           #Konverterer verdiene i datolistetrykk til datetime-objekter i lista datolistedatetimetrykk
    datolistedatetimetrykk.append(datetime.datetime.strptime(dato, format2))

temperaturarray1 = np.array(temperaturliste2)         #Lager arrays av dei forskjellige listene for plotting
lufttrykkarray1 = np.array(lufttrykk2)
temperaturarray2 = np.array(temperaturliste4)
abstrykkarray = np.array(absoluttrykk2) * 10          #Gongar verdiane i trykkverdiane med 10 i fil2
lufttrykkarray2 = np.array(lufttrykk4) * 10           #Sidan format er forskjellig mellom fil1 og fil2
datoarray1 = np.array(datolistedatetime)
datoarray2 = np.array(datolistedatetime2)
datoarray3 = np.array(datolistedatetimetrykk)

def stoy_reduksjon(tider: list, temperaturer: list, n: int):
    tidspunkter = list() # Lager en tom liste for tidspunkter
    gjennomsnittsverdier = list() # Lager en tom liste for gjennomsnittsverdier
    for i in range(len(temperaturer)): # Går gjennom alle temperaturer
        if i - n >= 0 and i + n < len(temperaturer): # Avgrenser til gyldige tidspunkter
            snitt = np.mean(temperaturer[i-n:i+n+1]) # Regner ut snittet av de n forrige målingene, den nåværende målingen og de n neste målingene
            tidspunkter.append(tider[i]) # Legger til tidspunktet i listen
            gjennomsnittsverdier.append(snitt) # Legger til snittet i listen
    return tidspunkter, gjennomsnittsverdier # Returnerer tidspunkter og gjennomsnittsverdier

# Beregn gjennomsnittet for hver tidsperiode ved hjelp av stoy_reduksjon-funksjonen
n = 30  # Antall verdier per gjennomsnitt
gjennomsnitt_tider, gjennomsnitt_temperaturer = stoy_reduksjon(datoarray2, temperaturarray2, n)

# Temperaturfall
fradato_index = datoliste2.index("06.11.2021 17:31")
tildato_index = datoliste2.index("06.12.2021 03:05")
liste_dato_fratil = list()
liste_temperaturer = list()
for i, u in enumerate(datoliste2):
    if fradato_index <= i <= tildato_index:
        liste_dato_fratil.append(datolistedatetime2[i])
        liste_temperaturer.append(temperaturliste4[i])
tempfall_maxtemp = max(liste_temperaturer)
tempfall_mintemp = min(liste_temperaturer)
tempfall_maxtemp_index = liste_temperaturer.index(tempfall_maxtemp)
tempfall_mintemp_index = liste_temperaturer.index(tempfall_mintemp)
tempfall_maxtemp_dato = liste_dato_fratil[tempfall_maxtemp_index]
tempfall_mintemp_dato = liste_dato_fratil[tempfall_mintemp_index]
liste_tempfall_temperatur = list()
liste_tempfall_dato = list()
liste_tempfall_temperatur.append(tempfall_maxtemp)
liste_tempfall_temperatur.append(tempfall_mintemp)
liste_tempfall_dato.append(tempfall_maxtemp_dato)
liste_tempfall_dato.append(tempfall_mintemp_dato)
array_tempfall_temp = np.array(liste_tempfall_temperatur)
array_tempfall_dato = np.array(liste_tempfall_dato)
speciallabel = "Temperaturfall 11.6 " + chr(0x2192) + " 12.6"

plt.subplot(2, 1, 1)                                  #Oppretter eit subplot til temperaturane og plotter dei
plt.ylabel("Temperatur")
plt.plot(datoarray1, temperaturarray1, color = "green", label = "Temperatur Sola")
plt.plot (datoarray2, temperaturarray2, color = "blue", label = "Temperatur UiS")
plt.plot(gjennomsnitt_tider, gjennomsnitt_temperaturer, color='orange', label='Gjennomsnittstemperatur', linewidth=1)
plt.plot(array_tempfall_dato,array_tempfall_temp, color = "magenta", label=speciallabel)
plt.legend()

plt.subplot(2, 1, 2)                                  #Oppretter eit subplot til trykkverdiane og plotter dei
plt.ylabel("Trykk hPa")
plt.xlabel("Tidspunkt")
plt.plot(datoarray1, lufttrykkarray1, color = "green", label = "Lufttrykk Sola")
plt.plot(datoarray3, lufttrykkarray2, color = "orange", label = "Lufttrykk UiS")
plt.plot(datoarray2, abstrykkarray, color = "blue", label = "Barometrisk trykk UiS")
plt.legend()
plt.show()
