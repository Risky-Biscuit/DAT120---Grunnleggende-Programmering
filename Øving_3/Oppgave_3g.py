"""
Script som bruker egendefinert funksjon: Lag et script som leser inn masse og fart fra
brukeren og så bruker funksjonen for kinetisk energi fra forrige deloppgave til å regne ut
kinetisk energi. Scriptet skal skrive ut den kinetiske energien.
"""

print("Vi skal regne ut den kinetiske energien til et legeme")

m = int(input("Hva er massen til legemet? "))
v = int(input("Hva er farten til legemet? "))

def kinetisk_energi(m, v):
    resultat = 0.5 * m * v**2
    return resultat


print(f"Den kinetiske energien til legemet er {kinetisk_energi(m,v)} joule.")
