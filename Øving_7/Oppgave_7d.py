"""
Frivillig: Stopp-ord. I informasjonsgjenfinning er stopp-ord ord som er så vanlige at de
ikke har særlig betydning for teksten. Dette gjelder typisk pronomen som «jeg» og småord
som «å», «en», «og» osv. Lag ei liste med stopp-ord og ikke ta med stopp-ordene når du
løser forrige deloppgave.
"""
# Tar inn filnavn fra brukeren
filename = input("Skriv inn filnavn: ")

# Lager et tomt dictionary for å lagre ordene og linjenumrene
words = {}

# Lager en liste med stopp-ord
stop_words = {
    "jeg", "å", "en", "og", "i", "på", "til", "av", "for", "med", "om", "at", "den", "det",
    "er", "som", "de", "du", "vi", "dere", "han", "hun", "det", "har", "hadde", "var", "ble",
    "blir", "ikke", "et", "eller", "så", "men", "om", "hvis", "når", "da", "der", "her", "hva",
    "hvem", "hvor", "hvordan", "hvorfor", "kan", "kunne", "skal", "skulle", "må", "måtte",
    "vil", "ville", "bør", "burde", "også", "alltid", "aldri", "ofte", "sjelden", "noen", "ingen",
    "noe", "ingenting", "hver", "hverandre", "mange", "få", "flere", "mest", "minst", "mer",
    "mindre", "slik", "sånn", "derfor", "dermed", "altså", "likevel", "dessuten", "imidlertid",
    "selv", "selv om", "uten", "innen", "utenfor", "innenfor", "over", "under", "mellom",
    "gjennom", "foran", "bak", "ved", "mot", "langs", "rundt", "omkring", "bort", "hjem",
    "hit", "dit", "ut", "inn", "opp", "ned", "fram", "tilbake", "både", "enten", "verken",
    "hverken", "enten", "eller", "både", "og", "verken", "eller"
}

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
                if word not in stop_words:
                    # Legger til ordet i dictionary
                    words[word] = line_number

# Skriver ut ordene og linjenumrene
for word, line_number in words.items():
    print(f"Ordet '{word}' forekommer første gang på linje {line_number}")
