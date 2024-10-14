"""
Fil som demonstrerer hvordan klasser kan brukes i Python.
"""

# Definer klassen 'Person'
class Person:
    # Konstruktør
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder

    # Metode for å skrive ut informasjon om personen
    def skriv_ut_info(self):
        print(f"Navn: {self.navn}, Alder: {self.alder}")

# Opprett et objekt av klassen 'Person'
person1 = Person("Ola", 23)

# Skriv ut informasjon om personen
person1.skriv_ut_info()

# Endre alderen til personen
person1.alder = 24

# Skriv ut informasjon om personen på nytt
person1.skriv_ut_info()

# Opprett et nytt objekt av klassen 'Person'
person2 = Person("Kari", 20)

# Skriv ut informasjon om personen
person2.skriv_ut_info()

# Endre alderen til personen
person2.alder = 21

# Skriv ut informasjon om personen på nytt
person2.skriv_ut_info()

# Skriv ut informasjon om personen på nytt
person1.skriv_ut_info()
