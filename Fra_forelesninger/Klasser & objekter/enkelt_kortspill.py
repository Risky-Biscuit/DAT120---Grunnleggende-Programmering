import random

# Klasse for å representere en spiller
class Spiller:
    def __init__(self, navn):
        self.navn = navn  # Spillerens navn
        self.kort = None  # Spillerens kort, initialisert til None

    def poengsum(self):
        # Returnerer poengsummen til spillerens kort
        return self.kort.verdi

    def __str__(self):
        # Returnerer en strengrepresentasjon av spilleren
        resultat = "Spiller " + self.navn
        if self.kort is None:
            resultat += " har ikke fått et kort enda"
        else:
            resultat += " har kortet: " + str(self.kort)
        return resultat


# Klasse for å representere et spillkort
class Spillkort:
    KLOVER = 1
    RUTER = 2
    HJERTER = 3
    SPAR = 4

    KONGE = 13
    DAME = 12
    KNEKT = 11

    def __init__(self, verdi, korttype):
        self.verdi = verdi  # Kortets verdi (1-13)
        self.korttype = korttype  # Kortets type (1-4)

    def __str__(self):
        # Returnerer en strengrepresentasjon av kortet
        resultat = "Ugyldig korttype! "
        if self.korttype == Spillkort.RUTER:
            resultat = "Ruter "
        if self.korttype == Spillkort.KLOVER:
            resultat = "Kløver "
        if self.korttype == Spillkort.HJERTER:
            resultat = "Hjerter "
        if self.korttype == Spillkort.SPAR:
            resultat = "Spar "
        if self.verdi == 1:
            resultat += "Ess"
        elif self.verdi > 1 and self.verdi <= 10:
            resultat += str(self.verdi)
        elif self.verdi == Spillkort.KNEKT:
            resultat += "Knekt"
        elif self.verdi == Spillkort.DAME:
            resultat += "Dame"
        elif self.verdi == Spillkort.KONGE:
            resultat += "Konge"
        else:
            resultat += "Ugyldig kortverdi"
        return resultat


# Klasse for å representere en kortstokk
class Kortstokk:
    def __init__(self):
        self.kortene = list()  # Liste for å holde kortene i kortstokken

    @property
    def overste_kort(self):
        # Returnerer det øverste kortet i kortstokken
        if len(self.kortene) == 0:
            return None
        return self.kortene[-1]

    def fyll_stokken(self):
        """Fyller kortstokken med de vanlige 52 spillkortene"""
        for korttype in range(1, 5):
            for verdi in range(1, 14):
                self.kortene.append(Spillkort(verdi, korttype))

    def stokk(self):
        # Stokker kortstokken
        random.shuffle(self.kortene)

    def trekk(self):
        # Trekker det øverste kortet fra kortstokken
        kortet = self.kortene[-1]
        del self.kortene[-1]
        return kortet

    def legg(self, kort):
        # Legger et kort til kortstokken
        self.kortene.append(kort)

    def lag_streng(self):
        # Returnerer en strengrepresentasjon av kortstokken
        resultat = "Kortstokk: \n"
        for kort in self.kortene:
            resultat += "  " + str(kort) + "\n"
        return resultat


# Funksjon for å lese inn et heltall fra brukeren
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


# Funksjon for å lage en kortstokk
# Kortstokken er ei liste hvor toppen av stokken er slutten av lista
def lag_kortstokken():
    kortstokk = list()
    for korttype in range(1, 5):
        for verdi in range(1, 14):
            kortstokk.append(Spillkort(verdi, korttype))
    random.shuffle(kortstokk)
    return kortstokk


# Funksjon for å trekke et kort fra kortstokken
def trekk_kort(kortstokk):
    kortet = kortstokk[-1]
    del kortstokk[-1]
    return kortet


# Funksjon for å sjekke hvem som vant
def sjekk_vinner(spiller_liste, kortstokk):
    """
    Sjekker hvem som vant. Tar inn ei liste med spillere og
    returnerer en referanse til spilleren som har vunnet.
    """
    fortsetter = True
    while fortsetter:
        forelopige_vinnere = list()
        forelopige_vinnere.append(spiller_liste[0])
        for i in range(1, len(spiller_liste)):
            if spiller_liste[i].poengsum() > forelopige_vinnere[0].poengsum():
                forelopige_vinnere.clear()
                forelopige_vinnere.append(spiller_liste[i])
            elif spiller_liste[i].poengsum() == forelopige_vinnere[0].poengsum():
                forelopige_vinnere.append(spiller_liste[i])
        if len(forelopige_vinnere) == 1:
            fortsetter = False
            return forelopige_vinnere[0]
        else:
            for spiller in forelopige_vinnere:
                spiller.kort = kortstokk.trekk()
            spiller_liste = forelopige_vinnere


if __name__ == "__main__":
    # Opprett en ny kortstokk, fyll den med kort og stokk den
    kortstokk = Kortstokk()
    kortstokk.fyll_stokken()
    kortstokk.stokk()
    print(kortstokk.lag_streng())

    # Opprett en liste for å holde spillerne
    spillerne = list()
    antall_spillere = les_inn_heltall("Skriv inn antall spillere: ")
    for i in range(1, antall_spillere + 1):
        navn = input(f"Skriv inn navnet til spiller {i}:")
        spilleren = Spiller(navn)
        spilleren.kort = kortstokk.trekk()
        spillerne.append(spilleren)

    # Skriv ut informasjon om hver spiller
    for spiller in spillerne:
        print(spiller)

    # Sjekk hvem som vant og skriv ut vinneren
    vinner = sjekk_vinner(spillerne, kortstokk)
    print("Vinneren ble: " + str(vinner))
