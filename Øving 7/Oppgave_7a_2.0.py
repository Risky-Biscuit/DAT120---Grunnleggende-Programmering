"""
Fjerning av duplikater: Lag et script som lar brukeren skrive inn ett eller flere ord.
Scriptet skal skrive ut alle bokstavene som ordet eller ordene brukeren skreiv inn
inneholder, men hver bokstav skal skrives ut bare en gang
"""

# Lager en input for ordet / ordene
input_string = input("Skriv inn ett eller flere ord: ")

# Gjør om strengen til et set
unique_characters = set(input_string)

# Printer ut ordene
print(f"Bokstavene det du skrev inneholdt er {unique_characters}")
