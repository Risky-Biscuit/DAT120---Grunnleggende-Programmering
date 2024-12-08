filnavn = input("Skriv inn navn på fila den skal lese inn: ")
try:
    with open(filnavn, "r", encoding="utf8") as innfil:
        valuta_inn = innfil.readline()
        print(f"Valuta inn: {valuta_inn}")
        valuta_ut = input("Skriv inn navn på valutaen den skal konvertere til: ")
        valutakurs = float(input("Valutakurs: "))
        ut_filnavn = input("Skriv inn navn på fila den skal skrive til: ")
        with open(ut_filnavn, "w", encoding="utf8") as utfil:
            utfil.write(valuta_ut + "\n")
            for linje in innfil:
                try:
                    belop = float(linje.strip())
                except ValueError:
                    continue
                ut_belop = belop * valutakurs
                utfil.write(str(ut_belop) + "\n")
except FileNotFoundError:
    print("Finner ikke fila som skal leses!")
except IOError:
    print("En feil oppstod i lesing av fila")
