# Enkel versjon av Punkt klassen

class Punkt:
    def __init__(self, x=0, y=0):
        self.x_koordinat = x
        self.y_koordinat = y

    def avstand_fra_origo(self):
        return (self.x_koordinat ** 2 + self.y_koordinat ** 2) ** 0.5

    # Spørremetode (Query)
    def avstand(self, punktet):
        x_avstand = self.x_koordinat - punktet.x_koordinat
        y_avstand = self.y_koordinat - punktet.y_koordinat
        return (x_avstand ** 2 + y_avstand ** 2) ** 0.5

    # Endremetode (Mutator)
    def flytt(self, delta_x, delta_y):
        self.x_koordinat += delta_x
        self.y_koordinat += delta_y

    # Strengrepresentasjon av punktet til ekstern bruk
    def __str__(self):
        return f"Punkt str: ({self.x_koordinat}, {self.y_koordinat})"

    # Strengrepresentasjon av punktet til intern bruk, ofte kortere enn __str__
    def __repr__(self):
        return f"Punkt repr: ({self.x_koordinat}, {self.y_koordinat})"
