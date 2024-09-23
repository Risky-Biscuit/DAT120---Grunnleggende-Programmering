tuppel = (1, 2, 3, 4, 5)

for i in tuppel:
    print(i)

print(tuppel[0])

# tuppel[1] = 10 # Dette vil gi en feilmelding siden tuppel er et uforanderlig objekt

# tuppel.append(6) # Dette vil gi en feilmelding siden tuppel er et uforanderlig objekt

tuppel = (1, 2, 3, 4, 5, 6) # Dette vil gå fint siden vi lager et nytt tuppel
print(tuppel)

liste2 = [1, 2, 3, 4, 5]

tuppel2 = tuple(liste2) # Dette vil også gå fint siden vi lager et nytt tuppel

print(tuppel2)