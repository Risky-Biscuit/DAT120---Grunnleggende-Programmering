"""
Lager en tom firkant av stjerner
"""

hoyde = int(input("Skriv inn høyde: "))
bredde = int(input("Skriv inn bredde: "))

for y in range(hoyde):
    if y == 0 or y == hoyde - 1:
        # Skriv ut full rad med stjerner på første og siste rad
        for x in range(bredde):
            print("*", end=" ")
    else:
        # Skriv ut stjerne først, mellomrom i midten, og en stjerne på slutten
        print("*", end=" ")
        for x in range(1, bredde - 1):
            print(" ", end=" ")
        print("*", end=" ")
    print()  # Gå til neste rad
