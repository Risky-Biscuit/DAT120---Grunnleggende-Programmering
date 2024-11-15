#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 18:04:35 2024

@author: nominomo
"""

import funksjoner
import matplotlib.pyplot as plt

# Definerer variabler:
# Filer/datakilder
datakilde_fil_uis = "data/trykk_og_temperaturlogg_rune_time.csv.txt"
datakilde_fil_sola = "data/temperatur_trykk_met_samme_rune_time_datasett.csv.txt"

# Startpunktet for første forekomst av datapunkt i datalistene
    # fra uis
datapunkt_startindex_uis_dato = 5
datapunkt_startindex_uis_sekunder = 6
datapunkt_startindex_uis_temp = 9
datapunkt_startindex_uis_lufttrykk = 7
datapunkt_startindex_uis_abs_trykk = 8
    # fra uis ... igjen (delen med annerledes datoformat) | Tenkte at gjerne det kan
indeksøkning_uis2 = 60490   # Med de samme startverdiene som over + denne verdien, stemmer det ut for alle i det nye formatet
datapunkt_startindex_uis2_dato =      datapunkt_startindex_uis_dato + indeksøkning_uis2
datapunkt_startindex_uis2_sekunder =  datapunkt_startindex_uis_sekunder + indeksøkning_uis2
datapunkt_startindex_uis2_temp =      datapunkt_startindex_uis_temp + indeksøkning_uis2
datapunkt_startindex_uis2_lufttrykk = datapunkt_startindex_uis_lufttrykk + indeksøkning_uis2
datapunkt_startindex_uis2_abs_trykk = datapunkt_startindex_uis_abs_trykk + indeksøkning_uis2
    # fra meteorologisk institutt
datapunkt_startindex_sola_dato = 7
datapunkt_startindex_sola_temp = 8
datapunkt_startindex_sola_lufttrykk = 9

# Sluttpunktet av relevante datapunkt i datalistene
datapunkt_cutoff_uis = 60495    #Fra denne indeksen følger et annet format
datapunkt_cutoff_uis2 = None    #Fra denne indeksen følger ingen innhold (strengt tatt unødvendig å definere)
datapunkt_cutoff_sola = 365     #Fra denne indeksen følger ekstrainfo ang. datasettet

# Datetimeformat for datalistene
datetime_format_uis = "%m.%d.%Y %H:%M"
datetime_format_uis2 = "%m/%d/%Y %H:%M:%S %p"
datetime_format_sola = "%d.%m.%Y %H:%M"


#Genererer lister som skal manipuleres
    #Store datalister fra individuelle datakilder:
liste_data_uis =                           funksjoner.innhent_data_fra_datakilde(datakilde_fil_uis)
liste_data_sola =                          funksjoner.innhent_data_fra_datakilde(datakilde_fil_sola)
    #Individuelle lister for spesifikke datapunkter fra relevant dataliste:
liste_str_dato_uis =                       funksjoner.listedeling(liste_data_uis, datapunkt_startindex_uis_dato, datapunkt_cutoff_uis)
liste_str_sekunder_siden_start_uis =       funksjoner.listedeling(liste_data_uis, datapunkt_startindex_uis_sekunder, datapunkt_cutoff_uis)
liste_str_dato_uis2 =                      funksjoner.listedeling(liste_data_uis, datapunkt_startindex_uis2_dato)
liste_str_lufttrykk_uis =                  funksjoner.listedeling(liste_data_uis, datapunkt_startindex_uis_lufttrykk)
liste_str_abs_trykk_uis =                  funksjoner.listedeling(liste_data_uis, datapunkt_startindex_uis_abs_trykk)
liste_str_temp_uis =                       funksjoner.listedeling(liste_data_uis, datapunkt_startindex_uis_temp)
liste_str_dato_sola =                      funksjoner.listedeling(liste_data_sola, datapunkt_startindex_sola_dato, datapunkt_cutoff_sola)
liste_str_temp_sola =                      funksjoner.listedeling(liste_data_sola, datapunkt_startindex_sola_temp, datapunkt_cutoff_sola)
liste_str_lufttrykk_sola =                 funksjoner.listedeling(liste_data_sola, datapunkt_startindex_sola_lufttrykk, datapunkt_cutoff_sola)

# Genererer datetime-lister (obs. For uis: Legger sammen begge formatene og legger til sekunder i datetime-objektet)
    # Først fra datolistene
liste_datetime_uis =                       funksjoner.konverter_til_datetime(liste_str_dato_uis, datetime_format_uis)
liste_datetime_uis2 =                      funksjoner.konverter_til_datetime(liste_str_dato_uis2, datetime_format_uis2)
liste_datetime_sola =                      funksjoner.konverter_til_datetime(liste_str_dato_sola, datetime_format_sola)
    # Reformaterer (blir konvertert til type:str)
liste_str_dato_uis =                       funksjoner.reformater_datetime_objekt(liste_datetime_uis, datetime_format_uis)
liste_str_dato_uis2 =                      funksjoner.reformater_datetime_objekt(liste_datetime_uis2, datetime_format_uis + ":%S")
liste_str_dato_sola =                      funksjoner.reformater_datetime_objekt(liste_datetime_sola, datetime_format_uis + ":%S")
    #Legger sekundene til uis-lista
liste_str_sekunder_uis =                   funksjoner.konverter_til_streng(
    funksjoner.reduser_sekunder_til_0_59(funksjoner.konverter_til_int(liste_str_sekunder_siden_start_uis)))
liste_str_dato_uis =                       funksjoner.merge_dato_m_sekund(liste_str_dato_uis, liste_str_sekunder_uis)
    #Legger sammen uis-listene
liste_str_dato_uis += liste_str_dato_uis2
  #Konverterer tilbake til datetime (nå har alt samme format)
liste_datetime_uis =                       funksjoner.konverter_til_datetime(liste_str_dato_uis, datetime_format_uis + ":%S")
liste_datatime_sola =                      funksjoner.konverter_til_datetime(liste_str_dato_sola, datetime_format_uis + ":%S")

# Konverterer datapunkter til flyttall og fjerner tomme datapunkter
liste_float_lufttrykk_uis =                funksjoner.konverter_til_float(
    funksjoner.bytt_ut_komma(filter(None, liste_str_lufttrykk_uis)))
liste_float_abs_trykk_uis =                funksjoner.konverter_til_float(
    funksjoner.bytt_ut_komma(liste_str_abs_trykk_uis))
liste_float_temp_uis =                     funksjoner.konverter_til_float(funksjoner.bytt_ut_komma(liste_str_temp_uis))
liste_float_temp_sola =                    funksjoner.konverter_til_float(funksjoner.bytt_ut_komma(liste_str_temp_sola))
liste_float_lufttrykk_sola =               funksjoner.konverter_til_float(
    funksjoner.bytt_ut_komma(liste_str_lufttrykk_sola))

# Genererer datetime lister som samsvarer med lufttrykk-listene ved å basere seg på indeksene i den oprinnelige innhentede lista lagret med streng-verdier
liste_datetime_lufttrykk_uis =             funksjoner.generer_datoliste_knyttet_til_datapunkt(liste_str_lufttrykk_uis, liste_datetime_uis)

#help, I can't tell what is wrong
plt.plot(liste_datetime_uis, liste_float_temp_uis, color = "red")
plt.show()
plt.plot(liste_datetime_uis, liste_float_abs_trykk_uis)
plt.show()
plt.plot(liste_datetime_lufttrykk_uis, liste_float_lufttrykk_uis)
plt.show()

# print(isinstance(liste_datetime_uis[1],datetime.datetime))
# print(isinstance(liste_datetime_uis2[1],datetime.datetime))
# print(isinstance(liste_datetime_sola[1],datetime.datetime))
# print(isinstance(liste_datetime_lufttrykk_uis[1],datetime.datetime))
# print(isinstance(liste_datetime_lufttrykk_uis2[1],datetime.datetime))








# Testkode for å sjekke at listene ser ok ut:
# listinquestion = liste_float_temp_uis                    # Should print 2digits,0-2digits
# listinquestion = liste_float_lufttrykk_uis               # Should print 3d,2d
# listinquestion = liste_float_abs_trykk_uis               # Should print 3d,3d
# listinquestion = liste_float_temp_uis2                   # Should print 2digits,0-2digits
# listinquestion = liste_float_lufttrykk_uis2              # Should print 3d,2d
# listinquestion = liste_float_abs_trykk_uis2              # Should print 3d,3d
# listinquestion = liste_float_temp_sola                   # Should print 2d,0/1d
# listinquestion = liste_float_lufttrykk_sola              # Should print 4d,0/1d
# print(listinquestion,"\nAntall: ",len(listinquestion))


# Testkode for å sjekke at det å bytte ut komma med punktum virker
# testliste = liste_temp_uis
# testliste = liste_temp_sola
# testliste = liste_lufttrykk_uis
# testliste = liste_lufttrykk_sola
# testliste = liste_abs_trykk_uis
# for i, value in enumerate(testliste):
    # print(funksjoner.bytt_ut_komma(testliste)[i]," | ",testlist[i])

# Testkode for å sjekke at verdier for lufttrykk og tilhørende dato har samme indeks (printes her, må sjekkes manuelt i datasett for å se at det stemmer)
# for index, value in enumerate(liste_datetime_lufttrykk_uis):
    # print(liste_datetime_lufttrykk_uis[index]," | ",liste_float_lufttrykk_uis[index])
