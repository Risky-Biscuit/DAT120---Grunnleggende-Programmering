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

def summer_og_beregn_gjennomsnitt():
    total_sum = 0
    antall_tall = 0

    while True:
        try:
            str = input("Skriv inn hvor mye det regnet i mm (én dag om gangen) / eventuelt skriv 'ferdig' for å si deg ferdig : ")
            if str == 'ferdig':
                break
            else:
                tall = int(str)
                if tall < 0:
                    tall = 0
                    total_sum += tall
                    antall_tall += 1
                    print(f"Foreløpig sum: {total_sum}")
                else:
                    total_sum += tall
                    antall_tall += 1
                    print(f"Foreløpig sum: {total_sum}")

        except ValueError:
            print("Vennligst skriv inn et gyldig heltall.")

    if antall_tall > 0:
        gjennomsnitt = total_sum / antall_tall
        print(f"Alle disse dagene har det totalt regnet {total_sum}mm.")
        print(f"Det har i gjennomsnitt regnet {gjennomsnitt:.2f}mm hver dag.")
    else:
        print("Ingen tall ble lagt inn.")


# Kjør programmet
summer_og_beregn_gjennomsnitt()
