"""
Dette skriptet demonstrerer forskjellige funksjoner og operasjoner som kan utføres med NumPy-biblioteket.
"""

import numpy as np

# Lager en array med 10 nuller
null_array = np.zeros(10)
print(null_array)

# Setter verdien på indeks 5 til 5.4
null_array[5] = 5.4
print(null_array)

# null_array[3] = "Hei" # Dette vil gi en feilmelding siden null_array er en array med tall

# Lager en array med 10 enere
one_array = np.ones(10)
print(one_array)

# Lager en array med tallene fra 10 til 50
range_array = np.arange(10, 51)
print(range_array)

# Lager en array med partall fra 10 til 50
even_array = np.arange(10, 51, 2)
print(even_array)

# Lager en 3x3 array med tallene fra 0 til 8
matrix_3x3 = np.arange(9).reshape(3, 3)
print(matrix_3x3)

# Lager en 3x3 identitetsmatrise
identity_matrix = np.eye(3)
print(identity_matrix)

# Lager en array med et tilfeldig tall mellom 0 og 1
random_array = np.random.rand(1)
print(random_array)

# Lager en array med 25 tilfeldige tall fra en normalfordeling
normal_dist_array = np.random.randn(25)
print(normal_dist_array)

# Lager en 10x10 array med tallene fra 0.01 til 1
linspace_array = np.linspace(0.01, 1, 100).reshape(10, 10)
print(linspace_array)

# Lager en array med 20 tall fra 0 til 1
linspace_20_array = np.linspace(0, 1, 20)
print(linspace_20_array)

# Finner det største tallet i linspace_20_array
print(linspace_20_array.max())

# Finner det minste tallet i linspace_20_array
print(linspace_20_array.min())

# Finner indeksen til det største tallet i linspace_20_array
print(linspace_20_array.argmax())

# Finner indeksen til det minste tallet i linspace_20_array
print(linspace_20_array.argmin())

# Finner dimensjonene til matrix_3x3
print(matrix_3x3.shape)

# Finner datatypen til matrix_3x3
print(matrix_3x3.dtype)

# Finner verdien på indeks (0, 0) i matrix_3x3
print(matrix_3x3[0, 0])

# Finner verdien på indeks (2, 2) i matrix_3x3
print(matrix_3x3[2, 2])

# Finner første rad i matrix_3x3
print(matrix_3x3[0])

# Finner første kolonne i matrix_3x3
print(matrix_3x3[:, 0])

# Finner en 2x2 array med de fire siste elementene i matrix_3x3
print(matrix_3x3[1:, 1:])

# Blokk med addisjon, subtraksjon, multiplikasjon og divisjon
print(matrix_3x3 + matrix_3x3) # Adderer matrix_3x3 med seg selv
print(matrix_3x3 - matrix_3x3) # Subtraherer matrix_3x3 med seg selv
print(matrix_3x3 * matrix_3x3) # Multipliserer matrix_3x3 med seg selv
print(matrix_3x3 / matrix_3x3) # Dividerer matrix_3x3 med seg selv

# Blokk med aritmetiske operasjoner med en konstant
print(matrix_3x3 + 1) # Adderer 1 til hvert element i matrix_3x3
print(matrix_3x3 - 1) # Subtraherer 1 fra hvert element i matrix_3x3
print(matrix_3x3 * 2) # Multipliserer hvert element i matrix_3x3 med 2
print(matrix_3x3 / 2) # Dividerer hvert element i matrix_3x3 med 2

# Blokk med matematiske funksjoner
print(np.sqrt(matrix_3x3)) # Tar kvadratroten av hvert element i matrix_3x3
print(np.exp(matrix_3x3)) # Tar e^x av hvert element i matrix_3x3
print(np.sin(matrix_3x3)) # Tar sinus av hvert element i matrix_3x3
print(np.cos(matrix_3x3)) # Tar cosinus av hvert element i matrix_3x3
print(np.log(matrix_3x3)) # Tar logaritmen av hvert element i matrix_3x3

# Blokk med aggregeringsfunksjoner
print(np.sum(matrix_3x3)) # Summerer alle elementene i matrix_3x3
print(np.sum(matrix_3x3, axis=0)) # Summerer elementene i hver kolonne i matrix_3x3
print(np.sum(matrix_3x3, axis=1)) # Summerer elementene i hver rad i matrix_3x3
print(np.mean(matrix_3x3)) # Finner gjennomsnittet av alle elementene i matrix_3x3
print(np.std(matrix_3x3)) # Finner standardavviket til alle elementene i matrix_3x3
print(np.median(matrix_3x3)) # Finner medianen til alle elementene i matrix_3x3
print(np.corrcoef(matrix_3x3)) # Finner korrelasjonskoeffisienten til matrix_3x3
print(np.var(matrix_3x3)) # Finner variansen til alle elementene i matrix_3x3

# Lager en 5x5 array med tallene fra 1 til 25
matrix_5x5 = np.arange(1, 26).reshape(5, 5)
print(matrix_5x5)

# Blokk med indeksering og slicing
print(matrix_5x5[2:, 1:]) # Finner en 3x4 array med de siste 12 tallene i matrix_5x5
print(matrix_5x5[3, 4]) # Finner tallet 20 i matrix_5x5
print(matrix_5x5[:3, 1:2]) # Finner en 3x1 array med tallene 2, 7 og 12 i matrix_5x5
print(matrix_5x5[4]) # Finner siste rad i matrix_5x5
print(matrix_5x5[3:]) # Finner de to siste radene i matrix_5x5

# Blokk med aggregeringsfunksjoner for matrix_5x5
print(matrix_5x5.sum()) # Summerer alle elementene i matrix_5x5
print(matrix_5x5.sum(axis=0)) # Summerer elementene i hver kolonne i matrix_5x5
print(matrix_5x5.sum(axis=1)) # Summerer elementene i hver rad i matrix_5x5
print(matrix_5x5.mean()) # Finner gjennomsnittet av alle elementene i matrix_5x5
print(matrix_5x5.mean(axis=0)) # Finner gjennomsnittet av elementene i hver kolonne i matrix_5x5
print(matrix_5x5.mean(axis=1)) # Finner gjennomsnittet av elementene i hver rad i matrix_5x5
print(matrix_5x5.std()) # Finner standardavviket til alle elementene i matrix_5x5
print(matrix_5x5.std(axis=0)) # Finner standardavviket til elementene i hver kolonne i matrix_5x5
print(matrix_5x5.std(axis=1)) # Finner standardavviket til elementene i hver rad i matrix_5x5
print(matrix_5x5.var()) # Finner variansen til alle elementene i matrix_5x5
print(matrix_5x5.var(axis=0)) # Finner variansen til elementene i hver kolonne i matrix_5x5
print(matrix_5x5.var(axis=1)) # Finner variansen til elementene i hver rad i matrix_5x5

# Blokk med maksimum og minimum funksjoner for matrix_5x5
print(matrix_5x5.max()) # Finner det største tallet i matrix_5x5
print(matrix_5x5.max(axis=0)) # Finner det største tallet i hver kolonne i matrix_5x5
print(matrix_5x5.max(axis=1)) # Finner det største tallet i hver rad i matrix_5x5
print(matrix_5x5.argmax()) # Finner indeksen til det største tallet i matrix_5x5
print(matrix_5x5.argmax(axis=0)) # Finner indeksen til det største tallet i hver kolonne i matrix_5x5
print(matrix_5x5.argmax(axis=1)) # Finner indeksen til det største tallet i hver rad i matrix_5x5
print(matrix_5x5.min()) # Finner det minste tallet i matrix_5x5
print(matrix_5x5.min(axis=0)) # Finner det minste tallet i hver kolonne i matrix_5x5
print(matrix_5x5.min(axis=1)) # Finner det minste tallet i hver rad i matrix_5x5
print(matrix_5x5.argmin()) # Finner indeksen til det minste tallet i matrix_5x5
print(matrix_5x5.argmin(axis=0)) # Finner indeksen til det minste tallet i hver kolonne i matrix_5x5
print(matrix_5x5.argmin(axis=1)) # Finner indeksen til det minste tallet i hver rad i matrix_5x5
