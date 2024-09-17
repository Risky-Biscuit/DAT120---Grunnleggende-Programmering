"""
Unntakshåndtering enkel: Skriv om programmet fra øving 2 oppgave a slik at det bruker
unntakshåndtering til å håndtere at brukeren skriver inn noe som ikke er et lovlig tall. Hvis
brukeren skriver inn noe som ikke er et lovlig tall skal brukeren få beskjed om det og få prøve
på nytt
"""
print("La oss dra på karusell! Først må vi bare sjekke om du er høy nok.")

while True:
    try:
        # En input for å legge inn høyden til personen
        hoyde = int(input("Hvor høy er du i cm? "))
        # Sjekker om personen er høy nok
        if hoyde >= 120:
            print("Du er høy nok. Ha det gøy! :D")
            break
        else:
            print("Du er dessverre ikke høy nok til å ride the rides :(")
            break
    # Passer på at koden ikke krasjer om man gir ugyldig input
    except ValueError:
        print("Verdien du skrev inn er ikke gyldig")
