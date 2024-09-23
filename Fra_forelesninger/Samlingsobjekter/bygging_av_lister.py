"""
This script demonstrates the use of list comprehension and importing functions from other modules.
It imports the `x_i_andre` function from `matematisk_funksjon` module and applies it to a list of odd numbers.
"""

from Fra_forelesninger.Funksjoner.matematisk_funksjon import x_i_andre

# List comprehension to create a list of squares of odd numbers from 1 to 10 using the imported function
liste = [x_i_andre(element) for element in range(1, 11) if element % 2 == 1]

# Liste = list()

# for element in range(1, 11):
#     if element%2 == 1:
#       liste.append(x_i_andre(element))

# Print the resulting list
print(liste)
