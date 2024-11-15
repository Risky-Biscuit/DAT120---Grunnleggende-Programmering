#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:50:50 2024

@author: nominomo
"""

import matplotlib as plt
import numpy as np
import datetime

#Funksjon som brukes til å innhente data fra ei fil
def innhent_data_fra_datakilde(filnavn: str):
    """
    liste av ALLE datapunkter splittet av newlines eller ";" symbolet.

    Parameters
    ----------
    filnavn : str
        Fila som skal brukes som datakilde.
        (Våre eneste kilder denne gang er disse):
            "data/trykk_og_temperaturlogg_rune_time.csv.txt"
            "data/temperatur_trykk_met_samme_rune_time_datasett.csv.txt"

    Returns
    -------
    populert_dataliste.
        Ferdig populert liste av Alle datapunkter.

    """
    populert_dataliste = list()
    with open(filnavn, "r") as fila:
        # i=-1 #Testlinje
        for lines in fila:
            # i+=1 #Testlinje
            maaling = lines.strip().split(";")                #Lager lister for hver måling/linje i datakilden
            for datapunkt in maaling:                         #Tar for seg enkeltverdiene/datapunktene fra hver måling/linje
                populert_dataliste.append(datapunkt)                   #Populerer den store datalista med hver enkelt datapunkt i hver måling.
                #print(i,"\ntype: ",type(enkeltverdi),"\nverdi: ",enkeltverdi,"\n") #Testlinje for å observere verdi-index, verditype, og selver verdien.
    return populert_dataliste


# Funksjon som populerer oppgitt liste med verdier fra en stor dataliste
def listedeling(dataliste: list, startindex = 0, sluttindex = None, stegverdi = 5):
    """


    Parameters
    ----------
    dataliste: list
        Den store datalisten som dataen skal hentes fra
    startindex : int
        Den indeksen i den store datalisten som først presenterer datatypen som skal innhentes.
    sluttindex : int
        Den indeksen ved slutten av dokumentet som har det siste datapunktet.
        (For å kutte av unødig ekstra i slutten av datakilden)
    stegverdi : int
        Det antallet indeksnummer som skal hoppes over før neste forekomst av datatypen.
        (Vil variere avhengig av datakilde)

    Returns
    -------
    populert_liste : list
        Den nylig genererte listen med fullstendig populert data.

    """

    populert_liste = list(dataliste[startindex : sluttindex : stegverdi])   #Funksjonen tar en startindex som er første gang et datapunkt dukker opp. Sluttverdi og stegverdi er basert på fila
    return populert_liste


# Funksjon for å generere ny datoliste som samsvarer til relevante datapunkter.
    #(vårt bruk denne gang: for lufttrykk og samsvarende dato)
def generer_datoliste_knyttet_til_datapunkt(verdiliste: list,datoliste: list):
    """


    Parameters
    ----------
    verdiliste : list
        Den først-initialiserte lista av verdier av én enkelt verditype.
            Brukes til å finne indeksen til alle reelle verdier.
    datoliste : list
        Den først-initialiserte dato-lista.
            brukes for å hente ut datoer til ny liste basert på indekser fra "verdilisten"

    Returns
    -------
    ny_datoliste : list
        Ny datoliste generert med kun datoer som samsvarer med reelle verdier fra "verdilisten".

    """
    ny_datoliste = list()
    for index, value in enumerate(verdiliste):
        if value != "":
            ny_datoliste.append(datoliste[index])
    return ny_datoliste

 # Funksjon som bytter ut komma med punktom for alle verdier i oppgitt liste
def bytt_ut_komma(liste: list):
    """


    Parameters
    ----------
    liste : list
        Listen som skal ha kommaene byttet ut med punktum.

    Returns
    -------
    updated_list : list
        Listen etter utbyttingen.

    """

    updated_list = list()
    for value in liste:
        updated_list.append(value.replace(",", "."))
    return updated_list


def konverter_til_int(liste: list):
    """


    Parameters
    ----------
    liste : list
        Den listen som skal ha verdiene konvertert til heltall.

    Returns
    -------
    oppdatert_liste : list
        Den nye listen av heltall.

    """
    oppdatert_liste=list()
    for value in liste:
        oppdatert_liste.append(int(value))
    return oppdatert_liste


def konverter_til_float(liste: list):
    """


    Parameters
    ----------
    liste : list
        Den listen som skal ha verdiene konvertert til flyttall.

    Returns
    -------
    oppdatert_liste : list
        Den nye listen av flyttall.

    """
    oppdatert_liste=list()
    for value in liste:
        oppdatert_liste.append(float(value))
    return oppdatert_liste


def konverter_til_streng(liste: list):
    """


    Parameters
    ----------
    liste : list
        Den listen som skal ha verdiene konvertert til strenger.

    Returns
    -------
    oppdatert_liste : list
        Den nye listen av strenger.

    """
    oppdatert_liste=list()
    for value in liste:
        oppdatert_liste.append(str(value))
    return oppdatert_liste


def merge_dato_m_sekund(datoliste: list, sekundliste: list):
    merged_datoliste = list()
    for i , dato in enumerate(datoliste):
        merged_datoliste.append(dato+":"+sekundliste[i])
    return merged_datoliste


def konverter_til_datetime(liste: list, datoformat: str):
    datetime_liste = list()
    for dato in liste:
        datetime_liste.append(datetime.datetime.strptime(dato, datoformat))
    return datetime_liste


def reformater_datetime_objekt(liste: list, datoformat: str):
    oppdatert_liste_str = list()
    for dato in liste:
        oppdatert_liste_str.append(dato.strftime(datoformat))
    return oppdatert_liste_str


def reduser_sekunder_til_0_59(liste: list):
    oppdatert_liste = list()
    for sekunder in liste:
        sekunder += 8
        while sekunder >= 60:
            sekunder -= 60
        oppdatert_liste.append(sekunder)
    return oppdatert_liste


# Relevant for deloppgave h:
# Funksjon som finner maks-, og min-temperatur fra opgitt datetime-objekt
    #Doesn't work in this state even at all slightly
def find_minmaxtemp_from_date(dato_fom: datetime, dato_tom: datetime, datoliste: list, temperaturliste: list):
    liste_indekser = list()
    liste_datetime_dato = list()
    liste_temperaturer = list()
    for i , dato in enumerate(datoliste):
        if dato.date() == dato_fom.date() or dato.date() == dato_tom.date():
            liste_indekser.append(i)
            liste_datetime_dato.append(dato)
            liste_temperaturer.append(temperaturliste[i])
    mintemp_index = liste_temperaturer.index(min)
    maxtemp_index = liste_temperaturer.index(max)
    mintemp = liste_temperaturer[mintemp_index]
    maxtemp = liste_temperaturer[maxtemp_index]
    mintemp_dato = liste_datetime_dato[mintemp_index]
    maxtemp_dato = liste_datetime_dato[maxtemp_index]
    return mintemp_dato, mintemp , maxtemp_dato, maxtemp
