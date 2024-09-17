def summer_og_beregn_gjennomsnitt():
    total_sum = 0
    antall_tall = 0

    while True:
        try:
            tall = int(input("Skriv inn et positivt heltall (eller et negativt tall for å avslutte): "))

            if tall < 0:
                break
            else:
                total_sum += tall
                antall_tall += 1
                print(f"Foreløpig sum: {total_sum}")

        except ValueError:
            print("Vennligst skriv inn et gyldig heltall.")

    if antall_tall > 0:
        gjennomsnitt = total_sum / antall_tall
        print(f"Den endelige summen er: {total_sum}")
        print(f"Gjennomsnittet av tallene er: {gjennomsnitt:.2f}")
    else:
        print("Ingen tall ble lagt inn.")


# Kjør programmet
summer_og_beregn_gjennomsnitt()
