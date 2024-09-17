"""
Program som lager en firkant av stjerner med linjer og X inni
"""

hoyde = int(input("Skriv inn høyde (bør være 5): "))
bredde = int(input("Skriv inn bredde (bør være 5): "))

for y in range(hoyde):
    if y == 0 or y == hoyde - 1:
        # Skriv ut full rad med stjerner på første og siste rad
        for x in range(bredde):
            print("*", end=" ")
    elif y == 1:
        # Skriv ut stjerne først, så en slash, mellomrom, backslash, og så en stjerne til slutt
        print("*", end=" ")
        print("\\", end=" ")
        print(" ", end=" ")
        print("/", end=" ")
        print("*", end=" ")
    elif y == 2:
        # Skriv ut en stjerne, så et mellomrom før en X, og så et nytt mellomrom før en stjerne
        print("*", end=" ")
        print(" ", end=" ")
        print("X", end=" ")
        print(" ", end=" ")
        print("*", end=" ")
    elif y == 3:
        # # Skriv ut stjerne først, så en backslash, mellomrom, slash, og så en stjerne til slutt
        print("*", end=" ")
        print("/", end=" ")
        print(" ", end=" ")
        print("\\", end=" ")
        print("*", end=" ")
    print()
