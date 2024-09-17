"""
Frivillig: Rainfall problem: Dette er en vanlig oppgave i grunnleggende programmering og er
en mer avansert variant av øving 2 oppgave d). Tanken er at brukeren skal skrive inn en serie
med verdier som representerer daglige målinger av nedbør. Etterpå skal programmet regne
ut total nedbør og gjennomsnittlig nedbør i perioden. For å løse denne, ta utgangspunkt i din
løsning på øving 2 oppgave d) og utvid den slik at den i tillegg håndterer følgende:
    a. Ugyldig brukerinput, inkludert ting som ikke er tall
    b. Den skal håndtere at brukeren skriver inn et negativt tall som første verdi uten å
    krasje med en ZeroDivisionError. Den skal i dette tilfellet skrive ut en total på 0 og at
    gjennomsnitt av 0 verdier er ugyldig
"""


print("Vi skal finne ut gjennomsnitlig nedor for en gitt periode.")
nedbor = str(input("Skriv inn mengden nedbor i mm for alle dagene du ønsker å finne gjennomsnittet av. Separer verdiene med mellomrom: "))
liste =  nedbor.split()
liste_med_tall = list(map(float, liste))
antall_dager = len(liste)
sum_nedbor = sum(liste_med_tall)
gjennomsnitt = sum_nedbor / antall_dager
print(f"Det har i gjennomsnitt regnet {gjennomsnitt} mm hver dag.")
