"""
Frivillig, avansert: I stedet for å bare skrive ut det første linjenummeret for hvert ord skal
programmet ditt i stedet skrive ut alle linjenumrene ordet forekommer. Hvert
linjenummer skal skrives ut bare en gang selv om ordet forekommer flere ganger på hver
linje. Ønsker du å være enda mer avansert kan du sjekke om ordet forekommer på flere
linjer etter hverandre og i så fall bare skrive ut det første av disse linjenumrene.
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
                words[word] = [line_number]
            else:
                if line_number not in words[word]:
                    words[word].append(line_number)

# Skriver ut ordene og linjenumrene
for word, line_numbers in words.items():
    print(f"Ordet '{word}' forekommer på linje(r) {line_numbers}")
