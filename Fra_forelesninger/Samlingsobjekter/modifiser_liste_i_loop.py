"""
This script iterates over a list, multiplies each element by 2, and inserts the result at the beginning of a new list.
"""

# Original list
liste = [2, 4, 6, 8, 10]

# New list to store the modified elements
ny_liste = list()

# Iterate over each element in the original list
for element in liste:
    print(element)  # Print the current element
    ny = element * 2  # Multiply the element by 2
    ny_liste.insert(0, ny)  # Insert the result at the beginning of the new list

# Print the new list with elements in reverse order, each multiplied by 2
print(ny_liste)