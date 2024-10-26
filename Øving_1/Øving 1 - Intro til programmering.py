avstand_kilometer = float(input("Skriv inn avstand i kilometer: "))
tid_minutter = float(input("Skriv inn tid i minutter: "))
tempo = tid_minutter / avstand_kilometer
fart = avstand_kilometer / (tid_minutter / 60)
print(f"Tempoet ditt var {tempo} minutter pr. kilometer")
print(f"Farten din var {fart} kilometer i timen")
