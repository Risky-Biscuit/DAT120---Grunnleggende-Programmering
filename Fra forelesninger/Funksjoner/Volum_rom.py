"""
Dette er et program man kan bruke til å finne areal og omkrets av et rom når man vet lengde og bredde
"""

def les_inn_tall(beskjed):
    fortsetter = True
    while fortsetter:
        tall_streng = (input(beskjed))
        try:
            tallet = float(tall_streng)
            fortsetter = False
        except ValueError:
            print(f"Tallet {tall_streng} er ikke gyldig.")
    return tallet


lengde = les_inn_tall("Hva er lengden av rommet målt i meter? ")
bredde = les_inn_tall("Hva er bredden av rommet målt i meter? ")
hoyde = les_inn_tall("Hva er hoyden av rommet målt i meter? ")

areal = lengde * bredde
omkrets = 2*lengde + 2*bredde
volum = areal * hoyde

print(f"Arealet av rommet blir {areal} kvadratmeter.")
print(f"Omkretsen av rommet blir {omkrets} meter.")
print(f"Volumet av rommet blir {volum} kubikkmeter.")
