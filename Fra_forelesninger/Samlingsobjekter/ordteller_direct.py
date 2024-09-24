"""
This script reads a text file and counts the occurrences of each word in the file.
The results are then printed to the console.
"""

# Initialize an empty dictionary to store word counts
ordliste = dict()

# Open the file in read mode with UTF-8 encoding
with open("/Users/kristiangundersen/PycharmProjects/DAT120 - Grunnleggende Programmering/Øving 1/Øving 1", "r",
          encoding="UTF-8") as file:
    # Iterate over each line in the file
    for linje in file:
        # Split the line into words
        ordene = linje.strip().split(" ")
        # Iterate over each word in the line
        for ord in ordene:
            # If the word is already in the dictionary, increment its count
            if ord in ordliste:
                antall = ordliste[ord]
                antall += 1
                ordliste[ord] = antall
            # If the word is not in the dictionary, add it with a count of 1
            else:
                ordliste[ord] = 1

# Print the word counts
for ord in ordliste:
    print(f"Ordet {ord} forekommer {ordliste[ord]} ganger i teksten.")