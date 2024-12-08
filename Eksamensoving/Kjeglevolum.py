from math import pi

radius = float(input("Hvor stor er radiusen til kjeglen? "))
hoyde = float(input("Hvor høy er kjeglen? "))

volum = (1/3)*pi*(radius**2)*hoyde

print(f"Volumet av kjeglen er {volum}.")
