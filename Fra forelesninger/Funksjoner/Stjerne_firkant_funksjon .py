"""
Program som lager en firkant av stjerner
"""

def stjerne_firkant(hoyde, bredde, tegn="*"):
    for y in range(hoyde):
        for x in range(bredde):
            print(tegn, end=" ")
        print()


# hoyde = int(input("Skriv inn hoyde: "))
# bredde = int(input("Skriv inn bredde: "))

stjerne_firkant(4, 5)
