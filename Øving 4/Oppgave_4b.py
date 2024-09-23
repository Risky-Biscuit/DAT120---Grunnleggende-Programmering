"""
Lese og skrive filer: Du skal skrive et Python-script som leser gjennom ei Python-scriptfil og
skriver ut alle funksjoner som blir definert i den fila. For å finne ut om ei linje inneholder
definisjonen av en funksjon, bruk <strengvariabel>.find(<delstreng>) metoden for å leite
etter ordet «def». Find() returnerer posisjonen til første bokstav i delstrengen i strengen i
strengvariabel, eller -1 om den ikke finner ordet. For hver funksjon, skriv ut linjenummer og
hele linja som inneholder funksjonsdefinisjonen
"""

with open("/Fra_forelesninger/Funksjoner/Stjerne_firkant_funksjon.py", "r", encoding="utf-8") as fil:
    for linjenummer, linje in enumerate(fil, start=1):  # enumerate gir oss både linjenummer og selve linjen
        if linje.find("def") !=-1:
            print(f"Linje {linjenummer}: {linje.strip()}")  # linje.strip() fjerner eventuelle unødvendige mellomrom
