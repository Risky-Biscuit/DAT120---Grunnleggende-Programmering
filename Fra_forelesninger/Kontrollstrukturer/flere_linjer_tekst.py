tekst = input("Skriv inn første linje: ")
linje = tekst
while linje != "":
    linje = input("Skriv inn neste linje: ")
    tekst += linje + "\n"
print("Ferdig")
print()
print(tekst)
