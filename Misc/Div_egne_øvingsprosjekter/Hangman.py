"""
Hangman spillet
"""

import random

# Ordbok med ord som kan velges
ordbok = ["hund", "katt", "fisk", "elefant", "giraff", "krokodille", "flodhest", "panda", "pingvin", "tiger",
          "løve", "bjørn", "ulv", "rev", "ape", "gorilla", "sjimpanse", "gibbon", "orangutang", "lemur", "neshorn",
          "flamingo", "struts", "papegøye", "due", "ørn", "falk", "hauk", "ugle", "spurv", "skjære", "kråke", "ravn",
          "gaupe", "jerv", "mår", "ilder", "ekorn", "mus", "rotte", "hamster", "marsvin", "kanin", "kattunge", "valp",
          "føll", "kalv", "killing", "lam", "føll", "brannslukningsapparatinstruksjonshåndbok", "kommunikasjonsproblemer",
          "kommunikasjonssvikt", "kommunikasjonsvansker", "kommunikasjonsproblematikk", "kommunikasjonsvanskeligheter",
          "vanskelighetsgrad", "fotball", "håndball", "basketball", "volleyball", "tennis", "bordtennis", "badminton",
          "friidrett", "svømming", "sykling", "skøyter", "skihopp", "langrenn", "alpint", "snowboard", "skiskyting",
          "orientering", "fekting", "bryting", "boksing", "karate", "taekwondo", "judo", "aikido", "kendo", "sumo",
          "boksing", "kickboksing", "muay thai", "krav maga", "selvforsvar", "selvforsvarsinstruksjon",]

# Velger et ord fra ordboken
valgt_ord = random.choice(ordbok)

# Antall forsøk spilleren har
antall_forsøk = 10

# Liste som holder styr på bokstavene spilleren har gjettet
bokstaver_gjettet = []

# Liste som representerer det gjettede ordet med plassholdere
gjettet_ord = ["_" for _ in valgt_ord]


print("Velkommen til Hangman")
print("Du har 10 forsøk på å gjette ordet.")
print("Lykke til!")

while antall_forsøk > 0:
    print("\n")
    print(" ".join(gjettet_ord))
    print(f"Du har {antall_forsøk} forsøk igjen.")
    gjettet_bokstav = input("Gjett en bokstav: ")

    if gjettet_bokstav in bokstaver_gjettet:
        print("Du har allerede gjettet denne bokstaven. Prøv en annen.")
        continue

    bokstaver_gjettet.append(gjettet_bokstav)

    if gjettet_bokstav in valgt_ord:
        for i, bokstav in enumerate(valgt_ord):
            if bokstav == gjettet_bokstav:
                gjettet_ord[i] = gjettet_bokstav
        if "_" not in gjettet_ord:
            print("Gratulerer! Du har gjettet ordet.")
            print(f"Ordet var {valgt_ord}.")
            break
    else:
        antall_forsøk -= 1
        print("Feil bokstav. Prøv igjen.")

if antall_forsøk == 0:
    print(f"Du har brukt opp alle forsøkene dine. Ordet var {valgt_ord}.")
    print("Game over.")
else:
    print("Takk for at du spilte Hangman.")
    print("Game over.")

print(f"Du gjettet følgende bokstaver: {bokstaver_gjettet}")