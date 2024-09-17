"""
Frivillig, avansert: Skriv en funksjon som finner ut om et år er et skuddår. Funksjonen skal ta
årstallet den skal sjekke som parameter. Funksjonen skal returnere en boolean, True hvis
året er et skuddår og False ellers. Skuddårsdefinisjon fra wikipedia: Et skuddår er normalt
hvert fjerde år – alle årstall som er delelige med 4 er skuddår, unntatt hundreårene (1700,
1800, 1900 osv.) som ikke er skuddår med mindre de er delelige med 400 (1600, 2000, 2400
etc.). Dermed ble 2000 et skuddår, mens 2100 ikke blir et skuddår
"""

aar = int(input("Skriv inn året du vil sjekke om er et skuddår: "))

if aar%400 == 0:
    print(f"År {aar} er et skuddår.")
elif aar%100 == 0:
    print(f"År {aar} er ikke et skuddår.")
elif aar%4 == 0:
    print(f"År {aar} er et skuddår.")
else:
    print(f"År {aar} er ikke et skuddår.")
