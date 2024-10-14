import math


# Avansert versjon av Punkt klassen med bruk av properties for å
# definere kulekoordinater og at x-koordinaten ikke kan være negativ.
class Punkt:
    def __init__(self, x=0, y=0):
        self.x_koordinat = x
        self.y_koordinat = y

    # Definerer x-koordinat som en property siden man da kan håndheve at den ikke
    # skal kunne være negativ
    @property
    def x_koordinat(self):
        return self.__x_koordinat

    @x_koordinat.setter
    def x_koordinat(self, ny_verdi):
        if ny_verdi < 0:
            raise ValueError("X-koordinaten kan ikke være negativ!")
        # Lager x-koordinaten i den private instansvariabelen self.__x_koordinat
        self.__x_koordinat = ny_verdi

    # Property for kulekoordinatet r, inkludert setter
    @property
    def r(self):
        return self.avstand_fra_origo()

    @r.setter
    def r(self, ny_verdi):
        theta = self.theta
        self.x_koordinat = ny_verdi * math.cos(theta)
        self.y_koordinat = ny_verdi * math.sin(theta)

    # Property for kulekoordinatet theta, uten setter slik at dette er
    # en egenskap som bare kan leses og ikke skrives til.
    @property
    def theta(self):
        return math.acos(self.x_koordinat / self.r)

    # Spørremetode
    def avstand_fra_origo(self):
        return (self.x_koordinat ** 2 + self.y_koordinat ** 2) ** 0.5

    def avstand(self, punktet):
        x_avstand = self.x_koordinat - punktet.x_koordinat
        y_avstand = self.y_koordinat - punktet.y_koordinat
        return (x_avstand ** 2 + y_avstand ** 2) ** 0.5

    # Strengrepresentasjon av punktet til ekstern bruk
    def __str__(self):
        return f"Punkt str: ({self.x_koordinat}, {self.y_koordinat})"

    # Strengrepresentasjon av punktet til intern bruk, ofte kortere enn __str__
    def __repr__(self):
        return f"Punkt repr: ({self.x_koordinat}, {self.y_koordinat})"


class RettLinje:
    def __init__(self, start: Punkt, slutt: Punkt):
        self.start = start
        self.slutt = slutt

    def lengde(self):
        return self.start.avstand(self.slutt)

    def __str__(self):
        return f"Linje: ({self.start.x_koordinat}, " + \
            f"{self.start.y_koordinat}) -> " + \
            f"({self.slutt.x_koordinat}, {self.slutt.y_koordinat})"


# Funksjon som modifiserer objektene den får inn
def flytt_til_midten(punkt1: Punkt, punkt2: Punkt):
    x_midt = (punkt1.x_koordinat + punkt2.x_koordinat) / 2
    y_midt = (punkt1.y_koordinat + punkt2.y_koordinat) / 2
    punkt1.x_koordinat = x_midt
    punkt2.x_koordinat = x_midt
    punkt1.y_koordinat = y_midt
    punkt2.y_koordinat = y_midt


# Funksjon som returnerer et objekt
def skriv_inn_punkt():
    x_koordinat = float(input("Skriv inn x_koordinat: "))
    y_koordinat = float(input("Skriv inn y_koordinat: "))
    punktet = Punkt(x_koordinat, y_koordinat)
    return punktet
