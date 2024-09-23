"""
Dette programmet gir en karakter basert på prosentscore på en prøve. Systemet er basert på samme som brukes på TEKNAT på UIS.
"""

prosentscore = int(input("Hvor mange prosent riktig, fra 0% - 100%, har eleven scoret på prøven? "))

if prosentscore >= 90:
    print("Gratulerer, du får karakteren A!")
elif 80 <= prosentscore < 90:
    print("Godt jobbet! Du får karatker B.")
elif 60 <= prosentscore < 80:
    print("Du får karakter C.")
elif 50 <= prosentscore < 60:
    print("Du får karakter D.")
elif 40 <= prosentscore < 50:
    print("Du får karakter E.")
else:
    print("Du stryker dessverre, og får karakter F.")
