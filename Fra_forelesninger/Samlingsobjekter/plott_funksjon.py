"""
This script demonstrates how to plot two different functions using Matplotlib.
The first plot shows the square of x-values, and the second plot shows a linear relationship.
"""

import matplotlib.pyplot as plt

# Define x-values
x_verdier = [-4, -3, -2, -1, 0, 1, 2, 3, 4]

# Calculate y-values for x squared
y_verdier = list()
for verdi in x_verdier:
    y_verdier.append(verdi**2)

# Calculate y-values for linear x
y_verdier_2 = list()
for verdi in x_verdier:
    y_verdier_2.append(verdi)

# Plot x squared
plt.plot(x_verdier, y_verdier, linestyle="dashed", marker="x", label="x i andre")

# Plot linear x
plt.plot(x_verdier, y_verdier_2, linestyle="solid", marker="o", label="linær")

# Add title and labels
plt.title("X i andre")
plt.xlabel("Verdi")
plt.ylabel("Resultat")

# Add legend
plt.legend()

# Show plot
# plt.savefig("figuren.pdf")  # Uncomment to save the figure as a PDF
plt.show()