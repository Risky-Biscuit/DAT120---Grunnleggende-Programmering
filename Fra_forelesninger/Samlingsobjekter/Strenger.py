"""
Dette er en gjennomgang av strenger
"""

strenger = "Strenger er lister av tegn"

# Vi kan bruke indeks på samme måte som i lister
print(f"Tredje tegnet i strengen er {strenger[2]}")
print(f"Tredje siste tegnet i strengen er {strenger[-2]}")

# Vi kan bruke strenger i for looper for å gå gjennom strengen tegn for tegn
for tegn in strenger:
    print(tegn)

# Vi kan sjekke lengden
print(f"Lengden av strengen er {len(strenger)} tegn.")

# Vi kan slice strenger
print(strenger[3:10])

# Vi kan ikke endre på strenger med .append, .insert eller .set elementet. Da får du TypeError
# En av grunnene til at strenger er uforanderlig er et ekstra lag med sikkerhet.

# Husk at vi kan gjøre strenger til .upper og .lower, og vi kan .replace i en streng

# Vi kan splitte en streng basert på ett eller flere enkelttegn
# Da returneres en liste med strenger
ordene = strenger.split(" ")
print(ordene)

# Vi kan også printe ut strengen ord for ord etter å ha splittet den
for element in ordene:
    print(element)

# Sidenote! En CSV-fil lagrer en tabell med data. Tenk et excel ark eller tilsvarende, kan lagres som CSV.
# CSV står for "comma separated values"
