"""
Frivillig, avansert: Utvid din løsning på oppgave b) og c) slik at den henter ut annen
informasjon fra Python-scriptet enn funksjoner slik som:
    a. Kommentarer: Se etter #-tegn
    b. Docstring: Se etter triple anførselstegn rett etter definisjonen av en funksjon. Merk
    at en docstring gjerne går over flere linjer. Den starter og slutter med triple
    anførselstegn, men det kan være flere linjer mellom start og slutt og alle linjene skal
    skrives ut.
    c. Variabeldefinisjoner: Se etter konstruksjoner av typen <variabel> = <uttrykk>. Merk
    at det ikke er noe problem å skrive ut samme variabel flere ganger hvis den blir
    tilordnet verdier i flere kodelinjer.
"""

try:
    with open("Oppgave_4a.py", "r", encoding="utf-8") as fil:
        inne_i_docstring = False  # Flaggvariabel for å holde styr på om vi er i en docstring
        docstring_innhold = []    # Liste for å samle opp docstring-linjer

        for linjenummer, linje in enumerate(fil, start=1):
            if linje.find("def") != -1:
                print(f"Definisjon funnet på linje {linjenummer}: {linje.strip()}")  # Funksjonsdefinisjon
            elif linje.find("#") != -1:
                print(f"Kommentar funnet på linje {linjenummer}: {linje.strip()}")  # Kommentar
            elif '"""' in linje:
                # Hvis vi allerede er inne i en docstring, er dette slutten
                if inne_i_docstring:
                    inne_i_docstring = False
                    docstring_innhold.append(linje.strip())  # Legg til slutten på docstring
                    # Skriv ut hele docstring
                    print(f"Docstring funnet på linje {linjenummer}:")
                    print("\n".join(docstring_innhold))
                    docstring_innhold = []  # Tøm docstring-innholdet for neste docstring
                else:
                    # Starten på docstring
                    inne_i_docstring = True
                    docstring_innhold.append(linje.strip())  # Start å samle linjer til docstring
            elif inne_i_docstring:
                # Hvis vi er inne i en docstring, legg til linjen
                docstring_innhold.append(linje.strip())
            # Ser etter '=' for å finne variabeldefinisjoner, men utelukker if statements, while- og for lokker og definisjoner
            elif "=" in linje and not ("==" in linje or "if" in linje or "for" in linje or "while" in linje or "def" in linje):
                # Split linjen på '=' for å hente ut variabelnavn og uttrykk
                variabel, uttrykk = linje.split("=", 1)  # Splitter på første '='
                print(f"Variabel funnet på linje {linjenummer}: {variabel.strip()} = {uttrykk.strip()}")


except FileNotFoundError:
    print("Kunne ikke finne filen som skal leses.")
except ValueError:
    print("Filen har feil format.")
except IOError:
    print("Filen er skadet.")
