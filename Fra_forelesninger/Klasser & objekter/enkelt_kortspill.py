import random

KLOVER = 1
RUTER = 2
HJERTER = 3
SPAR = 4

KONGE = 13
DAME = 12
KNEKT = 11


class Spiller:
    def __init__(self, navn):
        self.navn = navn
        self.kort = None

    def __str__(self):
        resultat = "Spiller " + self.navn
        if self.kort is None:
            resultat += " har ikke fått et kort enda"
        else:
            resultat += str(self.kort)
        return resultat


# Verdi = kortverdien, tallverdien på kortet hvis det er et tallkort.
# Bildekortene var verdiene 11, 12 og 13.
# Korttype = hjerter, ruter, spar eller kløver
class Spillkort:
    def __init__(self, verdi, korttype):
        self.verdi = verdi
        self.korttype = korttype

    def __str__(self):
        resultat = "Ugyldig korttype! "
        if self.korttype == RUTER:
            resultat = "Ruter "
        if self.korttype == KLOVER:
            resultat = "Kløver "
        if self.korttype == HJERTER:
            resultat = "Hjerter "
        if self.korttype == SPAR:
            resultat = "Spar "
        if self.verdi == 1:
            resultat += "Ess"
        elif self.verdi > 1 and self.verdi <= 10:
            resultat += str(self.verdi)
        elif self.verdi == KNEKT:
            resultat += "Knekt"
        elif self.verdi == DAME:
            resultat += "Dame"
        elif self.verdi == KONGE:
            resultat += "Konge"
        else:
            resultat += "Ugyldig kortverdi"
        return resultat


def les_inn_heltall(beskjed: str):
    fortsetter = True
    while fortsetter:
        tall_streng = input(beskjed)
        try:
            tallet = int(tall_streng)
        except ValueError:
            print(f"{tall_streng} er ikke et gyldig heltall! Prøv igjen!")
        else:
            fortsetter = False
    return tallet


def lag_kortstokken():
    kortstokk = list()
    for korttype in range(1, 5):
        for verdi in range(1, 14):
            kortstokk.append(Spillkort(verdi, korttype))
    random.shuffle(kortstokk)
    return kortstokk


if __name__ == "__main__":
    kortstokk = lag_kortstokken()
    spillerne = list()
    for kort in kortstokk:
        print(kort)

    antall_spillere = les_inn_heltall("Skriv inn antall spillere: ")
    for i in range(1, antall_spillere + 1):
        navn = input(f"Skriv inn navnet til spiller {i}:")
        spilleren = Spiller(navn)
        spillerne.append(spilleren)

    for spiller in spillerne:
        print(spiller)
