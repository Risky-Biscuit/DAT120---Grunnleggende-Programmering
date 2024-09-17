"""
Dette er et eksempel på hvordan man kan gjøre basis plotting
"""
import matplotlib.pyplot as plt

x_koordinater = [1, 2, 3, 4, 5]
y_koordinater = [4, 6, 7, 6, 5]

plt.plot(x_koordinater, y_koordinater, "o-")    # Tredje parameter er "stil".
# o- betyr at punktene skal være "o" og det skal være streker mellom punktene.
plt.show()
