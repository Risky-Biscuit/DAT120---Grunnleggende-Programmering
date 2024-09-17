"""
Program for å sjekke hvilken pris man skal betale for bussbillett
"""


alder = int(input("Hvor gammel er du? "))   # Spør hvor gammel personen er
if alder < 18:
    print("Din pris er 23kr, da du er under 18 år gammel.")     # U18 betaler 23kr
elif 18 <= alder <= 31:
    student = str(input("Er du student? "))     # Sjekk om student
    if student == "Ja":
        print("Din pris er 23kr, da du er student.")    # Student betlaer 23kr
    else:
        vernepliktig = str(input("Er du vernepliktig? "))   # Sjekk om vernepliktig
        if vernepliktig == "Ja":
            print("Din pris er 23kr, da du er vernepliktig.")   # Vernepliktig betaler 23kr
        if vernepliktig == "Nei":
            print("Din pris er 45kr.")      # Andre betaler 45kr
elif alder >= 67:
    print("Din pris er 23kr, da du er over pensjonsalderen som er 67 år gammel.")
else:
    vernepliktig = str(input("Er du vernepliktig? "))       # Sjekk om vernepliktig
    if vernepliktig == "Ja":
        print("Din pris er 23kr, da du er vernepliktig.")       # Vernepliktig betaler 23kr
    if vernepliktig == "Nei":
        print("Din pris er 45kr.")      # Andre betaler 45kr
