"""
Numpy arrayer: Lag en numpy array med alle heltallene fra og med -10 til og med 10. Lag
en ny numpy array hvor du kjører funksjonen fra den utdelte kodefila
oppgave_b_utdelt.py på hvert element i forrige array. Plott resultatet med første array på
x-aksen og andre array på y-aksen. Gjør det samme en gang til i et nytt subplott, men
hvor du har avstand 0.5 mellom verdiene i den første numpy arrayen.
"""

import numpy as np
import matplotlib.pyplot as plt
from Oppgave_b_utdelt import formel

# Lager en numpy array med alle heltallene fra og med -10 til og med 10
x = np.arange(-10, 11)

# Lager en ny numpy array hvor jeg kjører funksjonen fra Oppgave_b_utdelt på hvert element i x
y = formel(x)

# Lager et plot med x på x-aksen og y på y-aksen
plt.subplot(2, 1, 1)
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")

# Lager en ny numpy array hvor jeg har avstand 0.5 mellom verdiene i x
x2 = np.arange(-10, 10.5, 0.5)

# Lager en ny numpy array hvor jeg kjører funksjonen fra Oppgave_b_utdelt på hvert element i x2
y2 = formel(x2)

# Lager et plot med x2 på x-aksen og y2 på y-aksen
plt.subplot(2, 1, 2)
plt.plot(x2, y2)
plt.xlabel("x")
plt.ylabel("f(x)")

# Viser plottene
plt.show()
