"""
Funksjon med flere parametere: Formelen for den kinetiske energien til et legeme er KE =
½mv2. Skriv en funksjon som regner ut kinetisk energi. Funksjonen skal ta masse (m) og fart
(v) som parametere. Funksjonen skal returnere den kinetiske energien
"""

print("Vi skal regne ut den kinetiske energien til et legeme")

def kinetisk_energi(m, v):
    resultat = 0.5 * m * v**2
    return resultat


print(f"Den kinetiske energien til legemet er {kinetisk_energi(50,25)} joule.")
