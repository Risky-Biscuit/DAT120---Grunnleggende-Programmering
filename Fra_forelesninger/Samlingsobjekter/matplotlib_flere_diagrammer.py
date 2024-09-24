"""
This script demonstrates how to create multiple types of plots using Matplotlib.
It includes a bar chart, a pie chart, and a histogram.
"""

import matplotlib.pyplot as plt
import random

# Define the grades and their corresponding counts
karakter = ["A", "B", "C", "D", "E", "F"]
antall = [5, 16, 35, 23, 13, 19]
farger = ["green", "blue", "yellow", "orange", "red", "purple"]

# List to store random values for the histogram
verdier = list()

# Create a bar chart
plt.subplot(2, 2, 1)
plt.bar(karakter, antall, color=farger)

# Create a pie chart
plt.subplot(2, 2, 2)
plt.xlabel("Karakter")
plt.ylabel("Antall elever med karakter")
plt.title("Fordeling av karakterer")
plt.pie(antall, labels=karakter, colors=farger)

# Generate random values for the histogram
for i in range(10000):
    tall = random.random() + random.random() + random.random()
    verdier.append(tall)

# Create a histogram
plt.subplot(2, 2, 3)
plt.hist(verdier, 20)

# Display all plots
plt.show()
