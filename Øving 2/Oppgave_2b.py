"""
Program for å sjekke hvilken pris man skal betale for bussbillett
"""

alder = int(input("Hvor gammel er du? "))
if alder < 18:
    print("Din pris er 23kr, da du er under 18 år gammel.")
elif alder >= 67:
    print("Din pris er 23kr, da du er over pensjonsalderen som er 67 år gammel.")
else:
    print("Din pris er 45kr.")
