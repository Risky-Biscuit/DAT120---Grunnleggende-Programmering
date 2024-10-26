"""
Program som lager en firkant av stjerner
"""

hoyde = int(input("Skriv inn høyde: "))
bredde = int(input("Skriv inn bredde: "))

x = 0
for y in range(hoyde):
    for x in range(bredde):
        print("*", end=" ")
    print()
