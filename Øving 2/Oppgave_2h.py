"""
Program for å sjekke hvilken måned det er
"""

maaned = int(input("Skriv inn et tall for en måned: "))

if maaned < 1 or maaned > 12:
    print("ugyldig måned")
else:
    print("Gyldig måned")

if 0 < maaned < 3 or maaned == 12:
    print("Måneden er i vintersesongen")
elif 2 < maaned < 6:
    print("Måneden er i vårsesongen")
elif 5 < maaned < 9:
    print("Måneden er i sommersesongen")
elif 8 < maaned < 12:
    print("Måneden er i høstsesongen")
