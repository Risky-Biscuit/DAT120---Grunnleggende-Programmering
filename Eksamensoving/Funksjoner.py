def innenfor_lovlig_spenn(tall):
    if tall < -100:
        return False
    if tall > 100:
        return False
    return True


def topper(liste):
    topp_liste = list()
    for index in range(2, len(liste)-2):
        topp = True
        for i in range(1, 3):
            if liste[index-i] >= liste[index]:
                topp = False
                break
            if liste[index+i] >= liste[index]:
                topp = False
                break
        if (liste[index] > liste[index-1] and liste[index] > liste[index-2] and liste[index] > liste[index+1] and
                liste[index] > liste[index+2]):
            topp_liste.append(index)
    return topp_liste


lista = [23, 25, 22, 29, 34, 32, 175, 26, 15, 12, 10, 12, 15, 13, -123, 14, 17, 16, 11]

if __name__=="__main__":
    # Deloppgave b
    temperatur = float(input("Skriv inn en temperatur: "))
    if innenfor_lovlig_spenn(temperatur):
        print("Temperaturen er lovlig")
    else:
        print("Temperaturen er utenfor det som er normalt på jorda.")
    # Deloppgave d
    ny_liste = list()
    for element in lista:
        if innenfor_lovlig_spenn(element):
            ny_liste.append(element)
    topp_liste = topper(ny_liste)
    for element in topp_liste:
        print(f"Indeks {element}: {ny_liste[element]}")
