"""
Unntakshåndtering filer: Håndter alle unntak som kan oppstå under filoperasjonene i
oppgave b)
"""

try:
    with open("/Users/kristiangundersen/PycharmProjects/DAT120 - Grunnleggende Programmering/Fra forelesninger/Funksjoner/Stjerne_firkant_funksjon.py", "r", encoding="utf-8") as fil:
        for linjenummer, linje in enumerate(fil, start=1):  # enumerate gir oss både linjenummer og selve linjen
            if linje.find("def") !=-1:
                print(f"Linje {linjenummer}: {linje.strip()}")  # linje.strip() fjerner eventuelle unødvendige mellomrom
except FileNotFoundError:
    print("Kunne ikke finne filen som skal leses.")
except ValueError:
    print("Filen har feil format.")
except IOError:
    print("Filen er skadet.")
