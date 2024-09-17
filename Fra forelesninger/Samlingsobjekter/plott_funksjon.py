import matplotlib.pyplot as plt

x_verdier = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
y_verdier = list()
for verdi in x_verdier:
    y_verdier.append(verdi**2)

y_verdier_2 = list()
for verdi in x_verdier:
    y_verdier_2.append(verdi)

plt.plot(x_verdier, y_verdier, linestyle="dashed", marker="x", label = "x i andre")
plt.plot(x_verdier, y_verdier_2, linestyle="solid", marker="o", label = "linær")
plt.title("X i andre")
plt.xlabel("Verdi")
plt.ylabel("Resultat")
plt.legend()
# plt.savefig("figuren.pdf")
plt.show()
