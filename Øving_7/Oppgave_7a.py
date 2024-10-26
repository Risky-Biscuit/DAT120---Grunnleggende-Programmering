"""
Fjerning av duplikater: Lag et script som lar brukeren skrive inn ett eller flere ord.
Scriptet skal skrive ut alle bokstavene som ordet eller ordene brukeren skreiv inn
inneholder, men hver bokstav skal skrives ut bare en gang
"""

# Tar inn input fra brukeren
input_string = input("Skriv inn ett eller flere ord: ")

# Lager en tom liste for å lagre bokstavene
letters = []

# Går gjennom hvert ord i input_string
for word in input_string.split():
    # Går gjennom hver bokstav i ordet
    for letter in word:
        # Konverterer bokstaven til liten bokstav
        letter = letter.lower()
        # Sjekker om bokstaven allerede er lagret i listen
        if letter not in letters:
            # Legger til bokstaven i listen
            letters.append(letter)

# Skriver ut bokstavene
print("Bokstavene som er brukt er: ", end="")
for letter in letters:
    print(letter, end="")
print()

# Ikke del av oppgaven, men printer også hvor mange forskjellige bokstaver som er brukt
print(f"Det er {len(letters)} bokstaver som er brukt")
