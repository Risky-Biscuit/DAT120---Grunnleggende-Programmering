def les_liste(liste):
    aarstalldict = dict()
    for element in liste:
        tallstrenger = element.split(":")
        aar = int(tallstrenger[0])
        tall = int(tallstrenger[1])
        if aar not in aarstalldict:
            aarstalldict[aar] = 0
        aarstalldict[aar] = aarstalldict[aar] + tall
    return aarstalldict


def skriv_sortert_liste(dictionary):
    nokkel_liste = list(dictionary.keys())
    nokkel_liste.sort()
    for nokkel in nokkel_liste:
        print(f"Årstall: {nokkel} gir verdi {dictionary[nokkel]}")


if __name__ == "__main__":
    liste = ["1984: 3", "1987: 6", "1979: 2", "1984: 2"]
    dictionary = les_liste(liste)
    skriv_sortert_liste(dictionary)
