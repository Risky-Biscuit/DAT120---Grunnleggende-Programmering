import matplotlib.pyplot as plt


liste = list()
liste.append(1)
liste.append(1)
for i in range(2, 10):
    liste.append(liste[i-1] + liste[i-2])

x_koordinater = list()
for i in range(1, len(liste)+1):
    x_koordinater.append(i)
plt.plot(x_koordinater, liste, "o-")
plt.show()
