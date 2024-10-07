"""
Demonstrerer bruk av set(). Det som er greit med set() er at det ikke tillater duplikater.
Set() kan inneholde andre verdier enn lister, som f.eks. tall, tekst, osv.
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
print(set_a.union(set_b))  # Output: {1, 2, 3, 4, 5}
print(set_b.union(set_a))  # Output: {1, 2, 3, 4, 5}

# Intersection
print(set_a & set_b)  # Output: {3}
print(set_a.intersection(set_b))  # Output: {3}
print(set_b.intersection(set_a))  # Output: {3}

# Difference
print(set_a - set_b)  # Output: {1, 2}
print(set_b - set_a)  # Output: {4, 5}
print(set_a.difference(set_b))  # Output: {1, 2}
print(set_b.difference(set_a))  # Output: {4, 5}

# Symmetric difference
print(set_a < set_b)  # Output: False
print(set_a > set_b)  # Output: False

"""
 Both are false because set_a and set_b have elements that are not in the other set.
 The < and > operators are used to check if a set is a proper subset or superset of another set, respectively.
 So set_a < set_b is equivalent to set_a.issubset(set_b) and set_a > set_b is equivalent to set_a.issuperset(set_b).
 
In simpler terms, set_a < set_b checks if all elements in set_a are also in set_b, and set_a > set_b checks if all 
elements in set_b are also in set_a.
"""