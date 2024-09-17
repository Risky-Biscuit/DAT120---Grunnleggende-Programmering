"""
Unntakshåndtering filer: Håndter alle unntak som kan oppstå under filoperasjonene i
oppgave b)
"""

try:
    with open("Oppgave_4a.py", "r", encoding="utf-8") as fil:
        for linjenummer, linje in enumerate(fil, start=1):  # enumerate gir oss både linjenummer og selve linjen
            if linje.find("print") !=-1:    # Velger å lete etter "print" i stedet for "def" da koden min ikke inneholder def
                print(f"Linje {linjenummer}: {linje.strip()}")  # linje.strip() fjerner eventuelle unødvendige mellomrom
except FileNotFoundError:
    print("Kunne ikke finne filen som skal leses.")
except ValueError:
    print("Filen har feil format.")
except IOError:
    print("Filen er skadet.")
