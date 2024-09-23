ytre_liste = list()
ytre_liste.append([1, 2, 3])
ytre_liste.append([4, 5, 6])
ytre_liste.append([7, 8, 9])

print(ytre_liste)

print(ytre_liste[1][2])  # Access the element at index 2 in the list at index 1
print(ytre_liste[2][0])  # Access the element at index 0 in the list at index 2
print(ytre_liste[0][1])  # Access the element at index 1 in the list at index 0
print(ytre_liste[2][2])  # Access the element at index 2 in the list at index 2

# These commands will give IndexError if the indexes are out of range
print(ytre_liste[3][0])     # IndexError: list index out of range
# print(ytre_liste[0][3])   # IndexError: list index out of range
# print(ytre_liste[2][3])   # IndexError: list index out of range
# print(ytre_liste[3][3])   # IndexError: list index out of range