"""
Demonstrerer bruk av set()
"""

# Creating a set from a list
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

# Creating a set from a string
text = "hello"
unique_characters = set(text)
print(unique_characters)  # Output: {'h', 'e', 'l', 'o'}

# Adding elements to a set
unique_numbers.add(6)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements from a set
unique_numbers.remove(3)
print(unique_numbers)  # Output: {1, 2, 4, 5, 6}

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
print(set_a | set_b)  # Output: {1, 2, 3, 4, 5}

# Intersection
print(set_a & set_b)  # Output: {3}

# Difference
print(set_a - set_b)  # Output: {1, 2}
