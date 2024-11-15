import numpy as np
import datetime

#Genererer en lang liste med alle verdier fra opgitt datasett/fil
def generer_dataliste_fra_fil(fil_inn:str,verdisplitter=";") -> list:
    liste_resultat = list()
    with open(fil_inn, "r") as fil1:
        try:
            for lines in fil1:                              #For hver linje i fil1
                verdi = lines.strip().split(verdisplitter)            #Fjern whitespace og split ord med ;
                for ord in verdi:                           #For ord i verdi
                    liste_resultat.append(ord)                  #Legg til ordet/datapunktet i liste_data_sola
        except FileNotFoundError:
            fil_inn = input("\n"+"The file does not exist, try again:")
        except UnicodeDecodeError:
            fil_inn = input("\n"+"File appears to be unreadable, please specify a readable file:")
        except PermissionError:
            fil_inn = input("\n"+"It appears you do nothave permission to access this file, try again:")
    return liste_resultat


#Funksjon som splitter inkommende datasett i lister av samme type data
def listedeling(dataliste:list, startverdi:int, sluttverdi:int, stegverdi:int) -> list:
    listenavn = dataliste[startverdi : sluttverdi : stegverdi]
    return listenavn


#Funksjon som konverterer listedata fra streng til flyttall, tar imot parameter for hvilket tegn som skal omgjøres til punktum.
def konverterfloat(liste_inn: list, tegnskifte_til_punktum=",") -> list:
    liste_resultat = list()
    for value in liste_inn:
        try:
            liste_resultat.append(float(value.replace(tegnskifte_til_punktum, "."))) # Her byttes eks. komma ut med punktum for å sikre flyttalsomgjøringen
        except(ValueError, AttributeError):
            liste_resultat.append(None)
    return liste_resultat


def stoy_reduksjon(tider: list, temperaturer: list, n: int):
    tidspunkter = list()            #Oppretter lister som data skal skrivast til
    gjennomsnittsverdier = list()
    standardavvikverdier = list()
    for i in range(len(temperaturer)):
        if i - n >= 0 and i + n < len(temperaturer):  #Der n verdier finst,køyr funksjonen som vanleg
            snitt = np.mean(temperaturer[i-n:i+n+1])
            standardavvik = np.std(temperaturer[i-n:i+n+1])
        elif i - n < 0:
            snitt = np.mean(temperaturer[i:n+i+1])
            standardavvik = np.std(temperaturer[i:n+i+1])
        elif i + n >= len(temperaturer):
            snitt = np.mean(temperaturer[i-n:len(temperaturer)])
            standardavvik = np.std(temperaturer[i-n:len(temperaturer)])
        tidspunkter.append(tider[i])
        gjennomsnittsverdier.append(snitt)
        standardavvikverdier.append(standardavvik)
    return tidspunkter, gjennomsnittsverdier, standardavvikverdier


def temperaturfall(datetimeliste:list,temperaturliste:list,intervall_startdato:datetime,intervall_sluttdato:datetime) -> list:
    intervall_datoliste = list()
    intervall_templiste = list()
    for index,dato in enumerate(datetimeliste):
        if intervall_startdato <= dato <= intervall_sluttdato:
            intervall_datoliste.append(dato)
            intervall_templiste.append(temperaturliste[index])
    maxtemp =        max(intervall_templiste)
    maxtemp_index =  intervall_templiste.index(maxtemp)
    maxtemp_dato =   intervall_datoliste[maxtemp_index]
    mintemp =        min(intervall_templiste)
    mintemp_index =  intervall_templiste.index(mintemp)
    mintemp_dato =   intervall_datoliste[mintemp_index]
    tempfall_temp_liste = [maxtemp,mintemp]
    tempfall_dato_liste = [maxtemp_dato,mintemp_dato]
    return tempfall_temp_liste, tempfall_dato_liste


# Funksjon for glidende gjennomsnitt
def glidende_gjennomsnitt(data, vindu=10):
    smoothed_data = []  # Liste for å lagre de glidende gjennomsnittsverdiene
    for i in range(len(data)):
        start = max(0, i - vindu)  # Startindeks for vinduet
        slutt = min(len(data), i + vindu + 1)  # Sluttindeks for vinduet
        gjennomsnitt = np.mean(data[start:slutt])  # Beregn gjennomsnittet for dataene i vinduet
        smoothed_data.append(gjennomsnitt)  # Legg til gjennomsnittet i listen
    return np.array(smoothed_data)  # Konverter listen til en NumPy-array og returner den


# Tar inn 3 lister som basis for å finne den første målingen pr. time for de tre listene
# Den siste parameteren spesifiserer en liste som poluleres med datoer om tom, eller brukes som referansepunkt for datointervall om populert
# slik at alle nye datasett blir kuttet ned til samme lengde med det samme dato-intervallet som opgitt
def en_maaling_per_time(datoliste,templiste,trykkliste,datoliste_ut) -> list:
    templiste_ut = list()
    trykkliste_ut = list()
    datosett = set(datoliste_ut)
    list_nr_1 = False
    if len(datosett)==0:
        list_nr_1 = True
    for dato, temp, trykk in zip(datoliste,templiste,trykkliste):
        if dato.time().minute == 0 \
        and temp != 0 and trykk != 0 \
        and not np.isnan(temp)\
        and not np.isnan(trykk):
            dato = dato.replace(second=0)
            if list_nr_1 == True and dato not in datosett:
                templiste_ut.append(temp)
                trykkliste_ut.append(trykk)
                datosett.add(dato)
                datoliste_ut.append(dato)
            elif list_nr_1 == False and dato in datosett:
                templiste_ut.append(temp)
                trykkliste_ut.append(trykk)
    return datoliste_ut,templiste_ut,trykkliste_ut
