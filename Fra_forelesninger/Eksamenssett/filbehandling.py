from charset_normalizer.constant import UTF8_MAXIMAL_ALLOCATION

elementer = list()

try:
    with open("/Users/kristiangundersen/PycharmProjects/DAT120 - Grunnleggende Programmering/Fra_forelesninger/Eksamenssett/elementer", "r") as elementfil:
        for linje in elementfil:
            try:
                tall = int(linje.strip())
            except ValueError:
                continue
            elementer.append(tall)
except FileNotFoundError:
    print("Finner ikke fila.")
    exit()
except IOError:
    print("Feil i lesing av fila.")
    exit()

with open("/Users/kristiangundersen/PycharmProjects/DAT120 - Grunnleggende Programmering/Fra_forelesninger/Eksamenssett/grupper", "r") as gruppefil:
    linjenummer = 0
    for linje in gruppefil:
        linjenummer += 1
        tallstrenger = linje.strip().split(",")
        for tallstreng in tallstrenger:
            tall = int(tallstreng)
            if tall in elementer:
                print(f"Linja {linjenummer} inneholder minst ett av elementene")
                break
