"""
Diamant av stjerner der bruker oppgir størrelse
"""

def tegn_enkeltlinje(linjenummer, sidelengde):
    for x in range(sidelengde - 1 - linjenummer):
        print(" ", end="")
    print("*", end="")
    for x in range(linjenummer):
        print(" ", end="")
    if linjenummer > 0:
        for x in range(linjenummer - 1):
            print(" ", end="")
        print("*", end="")
    print()


sidelengde = int(input("Skriv inn lengden til sidene: "))

for y in range(sidelengde):
    tegn_enkeltlinje(y, sidelengde)
for y in range(sidelengde -2, -1, -1):
    tegn_enkeltlinje(y, sidelengde)
