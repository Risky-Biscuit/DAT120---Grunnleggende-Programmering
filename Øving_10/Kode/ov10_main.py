import ov10_funksjoner as ov10f
import matplotlib.pyplot as plt
import numpy as np
import datetime

# VARIABLER
###############################################################################
# Spesifiserer filene/datasettene som skal tas inn og konverteres til lister av verdier
SOLA_FIL="/Users/kristiangundersen/PycharmProjects/DAT120 - Grunnleggende Programmering/Øving_10/data/temperatur_trykk_met_samme_rune_time_datasett.csv.txt"
UIS_FIL="/Users/kristiangundersen/PycharmProjects/DAT120 - Grunnleggende Programmering/Øving_10/data/trykk_og_temperaturlogg_rune_time.csv.txt"
SINNES_SAUDA_FIL="/Users/kristiangundersen/PycharmProjects/DAT120 - Grunnleggende Programmering/Øving_10/data/temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv.txt"
# Beskriver hvor (indeksen) i den først importerte listen av datasettet de spesifikke datatypene opptrer
# SOLA
START_SOLA_DATO=7
START_SOLA_TEMP=8
START_SOLA_TRYKK=9
# UIS
START_UIS_DATO=5
START_UIS_TEMP=9
START_UIS_TRYKK=7
START_UIS_ABSTRYKK=8
# SINNES
START_SINNES_DATO=7
START_SINNES_TEMP=8
START_SINNES_TRYKK=9
# SAUDA
START_SAUDA_DATO=487
START_SAUDA_TEMP=488
START_SAUDA_TRYKK=489
# Beskriver indeksen hvor datapunkter ikke lenger inkluderes (enten for å kutte bort fluff, eller skille datasett i delt fil)
SOLA_CUTOFF=365
UIS_CUTOFF=None
SINNES_CUTOFF=485
SAUDA_CUTOFF=965
#Beskriver indeks-økningen før neste opptreden av den samme datatypen (tilfeldigvis lik for alle filer så langt)
DEFAULT_STEP_SOLA=5
DEFAULT_STEP_UIS=5
DEFAULT_STEP_SINNES=5
DEFAULT_STEP_SAUDA=5
# Beskriver de forskjellige dato-formatene brukt ved forskjellige punkter i datakilden (Brukes til å konvertere dato-strenger til datetime)
DATOFORMAT_SOLA =    "%d.%m.%Y %H:%M"
DATOFORMAT_UIS1 =    "%m.%d.%Y %H:%M"         #06.12.2021 22:36
DATOFORMAT_UIS2 =    "%m/%d/%Y %H:%M:%S %p"   #06/13/2021 00:00:08 am (denne burde sagt 12am for å passe det nye formatet)
DATOFORMAT_UIS3 =    "%m/%d/%Y %I:%M:%S %p"   #06/13/2021 10:31:08 pm
DATOFORMAT_SINNES =  "%d.%m.%Y %H:%M"
DATOFORMAT_SAUDA =   "%d.%m.%Y %H:%M"
DATOFORMAT_PRINT =   "%a %d.%m.%y %H%M"
#Beskriver antallet nærliggende datapunkter som skal brukes for beregning av gjennomsnittsverdi (støyreduksjonsfunksjonen)
STOYRED_ANT_MAALINGER = 60
#Beskriver øverste og nederste grense for hvor i dataene vi leter etter temperaturfall
TEMPFALL_DATOINTERVALL_START = datetime.datetime(year=2021,month=6,day=11,hour=0,minute=0,second=0)
TEMPFALL_DATOINTERVALL_SLUTT = datetime.datetime(year=2021,month=6,day=12,hour=10,minute=0,second=0)

#INITIALISERTE DICTIONARIES
###############################################################################
initial_str_val = dict() # Vil lagre sub-dictionaries for hver værstasjon som inneholder lister (av samme lengde) med de initielle strengverdiene av hver datatype
formatted_val = dict()   # Vil lagre sub-dictionaries for hver værstasjon som inneholder lister (av samme lengde) med formaterte verdier.
formatted_arrays = dict() # Vil lagre sub-dictionaries for hver værstasjon som inneholder numpy-arrays (av samme lengde) med ferdig-formaterte verdier.
presentable = {"uis_trykk":{},"uis_avg":{},"uis_trykkdifferanse":{},"uis_tempfall":{},"sola_tempfall":{}} #Vil holde subdicts av grupperte data som skal plottes
#DATA-INNHENTING
###############################################################################
#Genererer datasett-spesifikke lister av alle individuelle strengverdier skilt med ";"
innhentede_datasett = {"sola"         : ov10f.generer_dataliste_fra_fil(SOLA_FIL),
                       "uis"          : ov10f.generer_dataliste_fra_fil(UIS_FIL),
                       "sinnes_sauda" : ov10f.generer_dataliste_fra_fil(SINNES_SAUDA_FIL)}

# Lagrer de initielle verdiene av alle datatyper i egne lister, sortert i nøstede dictionaries for hver stasjon.
initial_str_val["sola"] =   {"dato"     : ov10f.listedeling(innhentede_datasett["sola"],START_SOLA_DATO, SOLA_CUTOFF, DEFAULT_STEP_SOLA),
                             "temp"     : ov10f.listedeling(innhentede_datasett["sola"],START_SOLA_TEMP, SOLA_CUTOFF, DEFAULT_STEP_SOLA),
                             "trykk"    : ov10f.listedeling(innhentede_datasett["sola"],START_SOLA_TRYKK, SOLA_CUTOFF, DEFAULT_STEP_SOLA)}

initial_str_val["uis"] =    {"dato"     : ov10f.listedeling(innhentede_datasett["uis"],START_UIS_DATO, UIS_CUTOFF, DEFAULT_STEP_UIS),
                             "temp"     : ov10f.listedeling(innhentede_datasett["uis"],START_UIS_TEMP, UIS_CUTOFF, DEFAULT_STEP_UIS),
                             "trykk"    : ov10f.listedeling(innhentede_datasett["uis"],START_UIS_TRYKK, UIS_CUTOFF, DEFAULT_STEP_UIS),
                             "abstrykk" : ov10f.listedeling(innhentede_datasett["uis"],START_UIS_ABSTRYKK, UIS_CUTOFF, DEFAULT_STEP_UIS)}

initial_str_val["sinnes"] = {"dato"     : ov10f.listedeling(innhentede_datasett["sinnes_sauda"],START_SINNES_DATO,SINNES_CUTOFF,DEFAULT_STEP_SINNES),
                             "temp"     : ov10f.listedeling(innhentede_datasett["sinnes_sauda"],START_SINNES_TEMP,SINNES_CUTOFF,DEFAULT_STEP_SINNES),
                             "trykk"    : ov10f.listedeling(innhentede_datasett["sinnes_sauda"],START_SINNES_TRYKK,SINNES_CUTOFF,DEFAULT_STEP_SINNES)}

initial_str_val["sauda"] =  {"dato"     : ov10f.listedeling(innhentede_datasett["sinnes_sauda"],START_SAUDA_DATO,SAUDA_CUTOFF,DEFAULT_STEP_SAUDA),
                             "temp"     : ov10f.listedeling(innhentede_datasett["sinnes_sauda"],START_SAUDA_TEMP,SAUDA_CUTOFF,DEFAULT_STEP_SAUDA),
                             "trykk"    : ov10f.listedeling(innhentede_datasett["sinnes_sauda"],START_SAUDA_TRYKK,SAUDA_CUTOFF,DEFAULT_STEP_SAUDA)}

#DATETIME-FORMATERING
###############################################################################
# Konverterer dato-listene til datetime og lagrer dem med nye nøkkler i dictionaryene til værstasjonene
formatted_val["sola"] =   {"dato" : [datetime.datetime.strptime(dato, DATOFORMAT_SOLA)   for dato in initial_str_val["sola"]["dato"]]}
formatted_val["sinnes"] = {"dato" : [datetime.datetime.strptime(dato, DATOFORMAT_SINNES) for dato in initial_str_val["sinnes"]["dato"]]}
formatted_val["sauda"] =  {"dato" : [datetime.datetime.strptime(dato, DATOFORMAT_SAUDA)  for dato in initial_str_val["sauda"]["dato"]]}

## Håndterer dato-format variasjonen i UIS-datasettet litt annerledes grunnet varierende datoformat
# datoliste_uis_split =   {1:[dato for dato in initial_str_val["uis"]["dato"] if initial_str_val["uis"]["dato"].index(dato) < initial_str_val["uis"]["dato"].index("06/13/2021 00:00:08 am")],
#                          2:[dato for dato in initial_str_val["uis"]["dato"] if initial_str_val["uis"]["dato"].index("06/13/2021 00:00:08 am") <= initial_str_val["uis"]["dato"].index(dato) < initial_str_val["uis"]["dato"].index("06/13/2021 01:00:08 am")],
#                          3:[dato for dato in initial_str_val["uis"]["dato"] if initial_str_val["uis"]["dato"].index("06/13/2021 01:00:08 am") <= initial_str_val["uis"]["dato"].index(dato)]}

# 3 datoformat, 3 lister, separert for bearbeiding
stasjon_uis_dato_split = {1:[],2:[],3:[]}
for dato in initial_str_val["uis"]["dato"]:
    targetkey = 1
    if targetkey == 1:
        if initial_str_val["uis"]["dato"].index(dato) >= initial_str_val["uis"]["dato"].index("06/13/2021 00:00:08 am"):
            targetkey = 2
    if targetkey == 2:
        if initial_str_val["uis"]["dato"].index(dato) >= initial_str_val["uis"]["dato"].index("06/13/2021 01:00:08 am"):
            targetkey = 3
    stasjon_uis_dato_split[targetkey].append(dato)

# Konverterer datoformatene individuelt til datetime
stasjon_uis_datetime_split =  {1 : [datetime.datetime.strptime(dato, DATOFORMAT_UIS1) for dato in stasjon_uis_dato_split[1]],
                               2 : [datetime.datetime.strptime(dato, DATOFORMAT_UIS2) for dato in stasjon_uis_dato_split[2]],
                               3 : [datetime.datetime.strptime(dato, DATOFORMAT_UIS3) for dato in stasjon_uis_dato_split[3]]}

# Slår dem sammen og lagrer slik som de andre værstasjonene
formatted_val["uis"] = {"dato" : list(stasjon_uis_datetime_split[1] + stasjon_uis_datetime_split[2] + stasjon_uis_datetime_split[3])}

#FLYTTALLKONVERTERING
###############################################################################
#Konverterer data fra str til float og lagrer som nye lister i dictionaries
formatted_val["uis"].update({"temp"     : ov10f.konverterfloat(initial_str_val["uis"]["temp"]),
                             "trykk_hpa"    : ov10f.konverterfloat(initial_str_val["uis"]["trykk"]),
                             "abstrykk_hpa" : ov10f.konverterfloat(initial_str_val["uis"]["abstrykk"])})

formatted_val["sola"].update({"temp"    : ov10f.konverterfloat(initial_str_val["sola"]["temp"]),
                              "trykk"   : ov10f.konverterfloat(initial_str_val["sola"]["trykk"])})

formatted_val["sinnes"].update({"temp"  : ov10f.konverterfloat(initial_str_val["sinnes"]["temp"]),
                                "trykk" : ov10f.konverterfloat(initial_str_val["sinnes"]["trykk"])})

formatted_val["sauda"].update({"temp"   : ov10f.konverterfloat(initial_str_val["sauda"]["temp"]),
                               "trykk"  : ov10f.konverterfloat(initial_str_val["sauda"]["trykk"])})

#Konverterer trykkmålingene i uis-datasettet fra hPa til kPa
formatted_val["uis"].update({"trykk":[],"abstrykk":[]})
for trykk, abstrykk in zip(formatted_val["uis"]["trykk_hpa"],formatted_val["uis"]["abstrykk_hpa"]):
    if trykk == None:
        formatted_val["uis"]["trykk"].append(None)
    else:
        formatted_val["uis"]["trykk"].append(trykk*10)
    formatted_val["uis"]["abstrykk"].append(abstrykk*10)

#KONVERTERING TIL ARRAY
###############################################################################
formatted_arrays["uis"] = {"dato"     : np.array(formatted_val["uis"]["dato"]),
                           "temp"     : np.array(formatted_val["uis"]["temp"]),
                           "trykk"    : np.array(formatted_val["uis"]["trykk"]),
                           "abstrykk" : np.array(formatted_val["uis"]["abstrykk"])}

formatted_arrays["sola"] = {"dato"    : np.array(formatted_val["sola"]["dato"]),
                            "temp"    : np.array(formatted_val["sola"]["temp"]),
                            "trykk"   : np.array(formatted_val["sola"]["trykk"])}

formatted_arrays["sinnes"] = {"dato"  : np.array(formatted_val["sinnes"]["dato"]),
                            "temp"    : np.array(formatted_val["sinnes"]["temp"]),
                            "trykk"   : np.array(formatted_val["sinnes"]["trykk"])}

formatted_arrays["sauda"] = {"dato"   : np.array(formatted_val["sauda"]["dato"]),
                            "temp"    : np.array(formatted_val["sauda"]["temp"]),
                            "trykk"   : np.array(formatted_val["sauda"]["trykk"])}

# Håndtering av de tomme variablene i trykk-målinger fra uis
uistrykkdato = []
uistrykk = []
uistemp_v_trykk = []
for dato, trykk, temp in zip(formatted_arrays["uis"]["dato"],formatted_arrays["uis"]["trykk"], formatted_arrays["uis"]["temp"]):
    if trykk is not None:  # Sjekker at trykk er gyldig (ikke null eller NaN)
        uistrykkdato.append(dato)
        uistrykk.append(trykk)
        uistemp_v_trykk.append(temp)

# Lagrer verdiene i egen sub-dictionary for strukturens skyld
presentable["uis_trykk"]["dato"] = np.array(uistrykkdato)
presentable["uis_trykk"]["trykk"] = np.array(uistrykk)
presentable["uis_trykk"]["temp"] = np.array(uistemp_v_trykk)
###############################################################################






###############################################################################

# Gjennomsnittstemperatur UIS (støyreduksjon)
presentable["uis_avg"]["dato"],presentable["uis_avg"]["temp"],presentable["uis_avg"]["stddev"] = ov10f.stoy_reduksjon(formatted_arrays["uis"]["dato"], formatted_arrays["uis"]["temp"], STOYRED_ANT_MAALINGER)

#Temperaturfall: Genererer lister med kun 2 datapunkt hver, én med maks/min temp, én med tilhørende datoer
presentable["uis_tempfall"]["temp"],presentable["uis_tempfall"]["dato"] = ov10f.temperaturfall(formatted_arrays["uis"]["dato"],presentable["uis_avg"]["temp"],TEMPFALL_DATOINTERVALL_START,TEMPFALL_DATOINTERVALL_SLUTT)
presentable["sola_tempfall"]["temp"],presentable["sola_tempfall"]["dato"] = ov10f.temperaturfall(formatted_arrays["sola"]["dato"],formatted_arrays["sola"]["temp"],TEMPFALL_DATOINTERVALL_START,TEMPFALL_DATOINTERVALL_SLUTT)

#BEREGNING AV DIFFERANSE MELLOM TRYKK OG ABSOLUTTRYKK UIS
###############################################################################
filtered_abstrykk = []
filtered_trykk = []
filtered_dato = []
# Iterer gjennom dataene og filtrer ut ugyldige linjer
for abstrykk, trykk, dato in zip(formatted_arrays["uis"]["abstrykk"],formatted_arrays["uis"]["trykk"], formatted_arrays["uis"]["dato"]):
    if trykk is not None:  # Sjekker at trykk er gyldig (ikke null eller NaN)
        filtered_abstrykk.append(abstrykk)
        filtered_trykk.append(trykk)
        filtered_dato.append(dato)

# Konverterer til arrays
filtered_abstrykk = np.array(filtered_abstrykk)
filtered_trykk = np.array(filtered_trykk)
filtered_dato = np.array(filtered_dato)

# Legger opp i dictionary for lesbarhet/struktur
presentable["uis_trykkdifferanse"]["dato"] = filtered_dato
# Beregn differansen mellom absolutt og barometrisk trykk
presentable["uis_trykkdifferanse"]["differanse"] = filtered_abstrykk - filtered_trykk
# Beregn glidende gjennomsnitt for differansen
presentable["uis_trykkdifferanse"]["differanse_smooth"] = ov10f.glidende_gjennomsnitt(presentable["uis_trykkdifferanse"]["differanse"], vindu=10)

#BEREGNING AV TEMPERATUR-, OG TRYKK-DIFFERANSE UIS-SOLA
###############################################################################
# Bruker funksjon som lager samsvarende lister for dato, temperatur, trykk, ved første måling pr. time hvor alle tre dataene opptrer
temp_trykk_forskjell_felles_datoliste = list()
# Første omgang populerer listen initiert over med alle datomålingene
# Andre omgang brukes listen som avgrensing av dato-intervallet slik at alle datoer utfor blir kuttet bort
# (altså må intervallet settes av det "korteste" datasettet for å skape like lange lister)
temp_trykk_forskjell_felles_datoliste,uis_temp_per_h,uis_trykk_per_h = ov10f.en_maaling_per_time(presentable["uis_trykk"]["dato"],presentable["uis_trykk"]["temp"],presentable["uis_trykk"]["trykk"], temp_trykk_forskjell_felles_datoliste)
temp_trykk_forskjell_felles_datoliste,sola_temp_per_h,sola_trykk_per_h = ov10f.en_maaling_per_time(formatted_arrays["sola"]["dato"],formatted_arrays["sola"]["temp"],formatted_arrays["sola"]["trykk"], temp_trykk_forskjell_felles_datoliste)

# Konverterer temperatur og trykk-listene med felles datointervall for å gjøre kalkulasjoner
uis_temp_deloppge = np.array(uis_temp_per_h)
uis_trykk_deloppge = np.array(uis_trykk_per_h)
sola_temp_deloppge = np.array(sola_temp_per_h)
sola_trykk_deloppge = np.array(sola_trykk_per_h)

# Kalkulerer og lagrer differansen som positive flyttall
array_tempforskjell_uis_sola = abs(uis_temp_deloppge - sola_temp_deloppge)
array_trykkforskjell_uis_sola = abs(uis_trykk_deloppge - sola_trykk_deloppge)

# Konverterer differansen til lister for å bruke listemetode
list_tempforskjell_uis_sola = [e for e in array_tempforskjell_uis_sola]
list_trykkforskjell_uis_sola = [e for e in array_trykkforskjell_uis_sola]

# Finner max/min-verdiene
max_tempforskjell_uis_sola =  max(list_tempforskjell_uis_sola)
min_tempforskjell_uis_sola =  min(list_tempforskjell_uis_sola)
max_trykkforskjell_uis_sola = max(list_trykkforskjell_uis_sola)
min_trykkforskjell_uis_sola = min(list_trykkforskjell_uis_sola)
# Finner alle indeksene hvor max/min opptrer
array_indexes_max_tempforskjell_uis_sola =  np.where(list_tempforskjell_uis_sola==max_tempforskjell_uis_sola)[0]
array_indexes_min_tempforskjell_uis_sola =  np.where(list_tempforskjell_uis_sola==min_tempforskjell_uis_sola)[0]
array_indexes_max_trykkforskjell_uis_sola = np.where(list_trykkforskjell_uis_sola == max_trykkforskjell_uis_sola)[0]
array_indexes_min_trykkforskjell_uis_sola = np.where(list_trykkforskjell_uis_sola == min_trykkforskjell_uis_sola)[0]
# Lager liste av dato/tid-målingene hvor max/min opptrer ut ifra indeksene
list_dato_max_tempforskjell_uis_sola =  [e.strftime(DATOFORMAT_PRINT) for i,e in enumerate(temp_trykk_forskjell_felles_datoliste) if i in array_indexes_max_tempforskjell_uis_sola]
list_dato_min_tempforskjell_uis_sola =   [e.strftime(DATOFORMAT_PRINT) for i,e in enumerate(temp_trykk_forskjell_felles_datoliste) if i in array_indexes_min_tempforskjell_uis_sola]
list_dato_storst_trykkforskjell_uis_sola = [e.strftime(DATOFORMAT_PRINT) for i,e in enumerate(temp_trykk_forskjell_felles_datoliste) if i in array_indexes_max_trykkforskjell_uis_sola]
list_dato_minst_trykkforskjell_uis_sola =  [e.strftime(DATOFORMAT_PRINT) for i,e in enumerate(temp_trykk_forskjell_felles_datoliste) if i in array_indexes_min_trykkforskjell_uis_sola]
# Beregner gjennomsnittsforskjellene av temp/trykk
gjennomsnittslig_tempforskjell_uis_sola = np.sum(array_tempforskjell_uis_sola)/len(array_tempforskjell_uis_sola)
gjennomsnittslig_trykkforskjell_uis_sola = np.sum(array_trykkforskjell_uis_sola)/len(array_trykkforskjell_uis_sola)

# Printer resultatene
print("---Temperaturforskjell mellom uis og sola---")
print(f"Størst forskjell: {max_tempforskjell_uis_sola:.3f} {list_dato_max_tempforskjell_uis_sola}")
print(f"Minst forskjell: {min_tempforskjell_uis_sola:.3f} {list_dato_min_tempforskjell_uis_sola}")
print(f"Gjennomsnittlig: {gjennomsnittslig_tempforskjell_uis_sola:.5f}"+"\n")
print("---Trykkforskjell mellom uis og sola---")
print(f"Størst: {max_trykkforskjell_uis_sola:.3f} {list_dato_storst_trykkforskjell_uis_sola}")
print(f"Minst: {min_trykkforskjell_uis_sola:.3f} {list_dato_minst_trykkforskjell_uis_sola}")
print(f"Gjennomsnittlig: {gjennomsnittslig_trykkforskjell_uis_sola:.5f}")

#PLOTTING
###############################################################################
# TEMP
plt.subplot(2, 1, 1)
plt.ylabel("Temperatur")
plt.plot(formatted_arrays["sinnes"]["dato"], formatted_arrays["sinnes"]["temp"], color = "cyan",linewidth=2, label = "Sinnes")
plt.plot(formatted_arrays["sauda"]["dato"], formatted_arrays["sauda"]["temp"], color = "red",linewidth=2, label = "Sauda")
plt.plot(formatted_arrays["sola"]["dato"], formatted_arrays["sola"]["temp"], color = "green",linewidth=2, label = "Sola")
# plt.plot(formatted_arrays["uis"]["dato"], formatted_arrays["uis"]["temp"], color = "blue",linewidth=2, label = "UiS") #Erstattet fullstendig med støyredusert
plt.plot(presentable["uis_avg"]["dato"],presentable["uis_avg"]["temp"], color='orange',linewidth=2, label='UiS.avg')
plt.plot(presentable["uis_tempfall"]["dato"],presentable["uis_tempfall"]["temp"], color = "black", linewidth=1, ls="--",label="Tempfall")
plt.plot(presentable["sola_tempfall"]["dato"],presentable["sola_tempfall"]["temp"], color = "black", linewidth=1, ls="--")
plt.legend()
# TRYKK
plt.subplot(2, 1, 2)
plt.ylabel("Trykk hPa")
plt.xlabel("Tidspunkt")
plt.plot(formatted_arrays["sinnes"]["dato"], formatted_arrays["sinnes"]["trykk"], color = "cyan", label = "Sinnes")
plt.plot(formatted_arrays["sauda"]["dato"], formatted_arrays["sauda"]["trykk"], color = "red", label = "Sauda")
plt.plot(formatted_arrays["sola"]["dato"], formatted_arrays["sola"]["trykk"], color = "green", label = "Sola")
plt.plot(presentable["uis_trykk"]["dato"], presentable["uis_trykk"]["trykk"], color = "blue", label = "UiS")
plt.plot(formatted_arrays["uis"]["dato"], formatted_arrays["uis"]["abstrykk"], color = "orange", label = "BaromUiS")
plt.legend()
plt.show()
# TRYKKDIFFERANSE UIS
plt.figure(figsize=(10, 6))
plt.plot(presentable["uis_trykkdifferanse"]["dato"], presentable["uis_trykkdifferanse"]["differanse"], label="Original Differanse", alpha=0.6)
plt.plot(presentable["uis_trykkdifferanse"]["dato"], presentable["uis_trykkdifferanse"]["differanse_smooth"], label="Smoothed Differanse", color="orange")
plt.xticks(ticks=presentable["uis_trykkdifferanse"]["dato"][::1000]) # Reduser antall etiketter på x-aksen (viser hver 1000. datapunkt)
plt.xlabel("Tidspunkt")
plt.ylabel("Differanse")
plt.title("Differanse mellom Absolutt og Barometrisk Trykk - UiS (Filtrert)")
plt.legend()
plt.grid()
plt.show()
# HISTOGRAM
bin_width = list()
for i in range(9, 23):
    bin_width.append(i)

plt.subplot(3, 1, 1)
plt.xlabel("Temperatur")
plt.hist(formatted_arrays["sola"]["temp"], bins = bin_width)
plt.subplot(3, 1, 2)
plt.xlabel("Temperatur")
plt.hist(formatted_arrays["uis"]["temp"], bins = bin_width)

# STANDARDAVVIK
plt.subplot(3, 1, 3)
plt.xlabel("Tidspunkt")
plt.ylabel("temperatur")
plt.errorbar(presentable["uis_avg"]["dato"],presentable["uis_avg"]["temp"], yerr=presentable["uis_avg"]["stddev"], capsize=3, errorevery=30)
plt.show()
