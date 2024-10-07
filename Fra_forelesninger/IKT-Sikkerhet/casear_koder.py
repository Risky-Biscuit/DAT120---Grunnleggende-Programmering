"""
Program som krypterer og dekrypterer en tekstfil med Caesar-kode.
"""

filnavn_inn = input("Skriv inn navn på fila inn: ")
filnavn_ut = input("Skriv inn navnet på fila ut: ")
distanse = int(input("Skriv inn hvor mange tegn den skal skifte. Negativ verdi for å dekryptere: "))

with open(filnavn_inn, "r") as inn_fil:
    with open(filnavn_ut, "w") as ut_fil:
        for linje in inn_fil:
            for tegn in linje:
                tegnkode = ord(tegn)
                if tegnkode >= ord("A") and tegnkode <= ord("Z"):
                    tegnkode += distanse
                    if tegnkode > ord("Z"):
                        tegnkode -= 26
                    if tegnkode < ord("A"):
                        tegnkode += 26
                if tegnkode >= ord("a") and tegnkode <= ord("z"):
                    tegnkode += distanse
                    if tegnkode > ord("z"):
                        tegnkode -= 26
                    if tegnkode < ord("a"):
                        tegnkode += 26
                ut_fil.write(chr(tegnkode))
            ut_fil.write("\n")
