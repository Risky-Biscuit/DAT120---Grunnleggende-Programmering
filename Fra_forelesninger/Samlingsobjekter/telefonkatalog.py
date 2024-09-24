"""
This module initializes a phone directory (telefonkatalog) and demonstrates basic dictionary operations in Python.

The phone directory stores names as keys and phone numbers as values. The module includes examples of adding
entries to the dictionary and retrieving phone numbers by name.
"""

# Initialize an empty dictionary to store phone numbers associated with names
telefonkatalog = dict()

# Add entries to the dictionary with names as keys and phone numbers as values
telefonkatalog["Jan Berg"] = "12345678"
telefonkatalog["Per Olsen"] = "87654321"
telefonkatalog["Kari Larsen"] = "56781234"

# Print the phone number associated with the key "Per Olsen"
print(telefonkatalog["Per Olsen"])

print(telefonkatalog.keys())
print(telefonkatalog.values())

for nokkel in telefonkatalog:
    print(nokkel, telefonkatalog[nokkel])
