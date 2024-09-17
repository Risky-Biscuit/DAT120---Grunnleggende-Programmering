def summer_positiv_tall():
    total_sum = 0

    while True:
        try:
            tall = int(input("Skriv inn et positivt heltall (eller et negativt tall for å avslutte): "))

            if tall < 0:
                break
            else:
                total_sum += tall
                print(f"Foreløpig sum: {total_sum}")

        except ValueError:
            print("Vennligst skriv inn et gyldig heltall.")

    print(f"Den endelige summen er: {total_sum}")


# Kjør programmet
summer_positiv_tall()
