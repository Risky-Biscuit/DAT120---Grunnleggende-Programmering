"""
En enkel kalkulator.
"""

try:
    valg = int(input("Hva ønsker du å gjøre? \n"
                     "1. Addisjon \n"
                     "2. Subtraksjon \n"
                     "3. Multiplikasjon \n"
                     "4. Divisjon \n"
                     "5. Avslutt \n"))

    if valg == 1 or 2 or 3 or 4:
        try:
            tall_1 = float(input("Skriv inn første tallet du vil utføre denne operasjonen på:"))
            tall_2 = float(input("Skriv inn andre tallet du vil utføre denne operasjonen på: "))

            if valg == 1:
                print(tall_1 + tall_2)
            elif valg == 2:
                print(tall_1 - tall_2)
            elif valg == 3:
                print(tall_1 * tall_2)
            elif valg == 4:
                print(tall_1 / tall_2)
        except ValueError:
            print("Det du skrev inn er ikke et tall. ")

    elif valg == 5:
        print("Programmet har blitt avsluttet.")
except ValueError:
    print("Ugyldig input! Det du skrev inn er ikke et tall")