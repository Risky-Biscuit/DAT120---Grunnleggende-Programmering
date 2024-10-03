"""
Dictionaries: Lag et program som leser gjennom ei tekstfil. For hvert ord i tekstfila skal
programmet registrere ordet og linjenummeret der ordet først forekommer i et dictionary.
Så skal programmet skrive ut ordene og linjenumrene. Du kan bygge løsningen din på
eksemplet «ordteller_dict.py» fra tema 9 samlingsobjekter. Dette eksemplet løser et
liknende problem. Oppgaveteksten til øving 1 og øving 6 som rein tekst er lagt ved
oppgaven.
"""
# Tar inn filnavn fra brukeren
filename = input("Skriv inn filnavn: ")

# Lager et tomt dictionary for å lagre ordene og linjenumrene
words = {}

# Åpner filen
with open(filename, "r") as file:
    # Går gjennom hver linje i filen
    for line_number, line in enumerate(file, 1):
        # Går gjennom hvert ord i linja
        for word in line.split():
            # Fjerner punktum og komma fra ordet
            word = word.strip(",.")
            # Konverterer ordet til små bokstaver
            word = word.lower()
            # Sjekker om ordet allerede er lagret i dictionary
            if word not in words:
                # Legger til ordet i dictionary
                words[word] = line_number

# Skriver ut ordene og linjenumrene
for word, line_number in words.items():
    print(f"Ordet '{word}' forekommer første gang på linje {line_number}")
