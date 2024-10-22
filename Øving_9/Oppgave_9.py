import matplotlib.pyplot as plt

class Maalinger_aar:
    def __init__(self, aar):
        self.aar = aar
        self.total_solflekker = 0
        self.antall_maalinger = 0
        self.maks_daglig = -float('inf')
        self.min_daglig = float('inf')

    def ny_maaling(self, antall_solflekker):
        self.total_solflekker += antall_solflekker
        self.antall_maalinger += 1
        if antall_solflekker > self.maks_daglig:
            self.maks_daglig = antall_solflekker
        if antall_solflekker < self.min_daglig:
            self.min_daglig = antall_solflekker

    def gjennomsnittlig_solflekker(self):
        return self.total_solflekker / self.antall_maalinger

# Dictionary for å lagre objekter av klassen Maalinger_aar
maalinger = {}

# Åpne filen med solflekkaktivitet
with open('data/solflekkaktivitet_daglig_excel.csv', 'r') as file:
    for line in file:
        # Split linjen for å hente ut kolonner (år og antall solflekker)
        data = line.strip().split(';')
        year = int(data[0])  # Kolonnen for år
        solflekker = int(data[4])  # Kolonnen for antall solflekker

        # Hopp over linjen hvis antall solflekker er -1
        if solflekker == -1:
            continue

        # Hvis året ikke finnes i dictionaryen, opprett et nytt objekt
        if year not in maalinger:
            maalinger[year] = Maalinger_aar(year)

        # Oppdater objektet med den nye målingen
        maalinger[year].ny_maaling(solflekker)

# Lister for plottet
years = []
average_solflekker = []
max_solflekker = []
min_solflekker = []

# Fyll opp listene ved å iterere gjennom dictionaryen
for year, maaling in maalinger.items():
    years.append(year)
    average_solflekker.append(maaling.gjennomsnittlig_solflekker())
    max_solflekker.append(maaling.maks_daglig)
    min_solflekker.append(maaling.min_daglig)

# Funksjon for å finne topper
def topper(years, average_solflekker, window=2):
    topp_aar = []
    for i in range(window, len(average_solflekker) - window):
        if all(average_solflekker[i] > average_solflekker[i - j] for j in range(1, window + 1)) and \
           all(average_solflekker[i] > average_solflekker[i + j] for j in range(1, window + 1)):
            topp_aar.append((years[i], average_solflekker[i]))
    return topp_aar

# Finn toppårene etter at listene er fylt
topp_aar = topper(years, average_solflekker, window=2)

# Beregn gjennomsnittlig avstand mellom toppene
def gjennomsnittlig_topp_avstand(topp_aar):
    if len(topp_aar) < 2:
        return 0  # Returner 0 hvis det ikke finnes nok topper til å beregne avstand

    # Beregn avstandene mellom påfølgende toppår
    avstander = [topp_aar[i + 1][0] - topp_aar[i][0] for i in range(len(topp_aar) - 1)]

    # Beregn gjennomsnittlig avstand
    gjennomsnitt_avstand = sum(avstander) / len(avstander)
    return gjennomsnitt_avstand

gjennomsnitt_avstand = gjennomsnittlig_topp_avstand(topp_aar)

# Skriv ut resultatet
print("Gjennomsnittlig avstand mellom toppene:", gjennomsnitt_avstand)

# Opprett plottet
plt.figure(figsize=(10, 6))
plt.plot(years, average_solflekker, label='Gjennomsnitt', color="black")
plt.plot(years, max_solflekker, label='Maksimum', color="orange", linestyle="dashed")
plt.plot(years, min_solflekker, label='Minimum', color="blue", linestyle="dashed")

# Marker toppårene med røde prikker
plt.plot([year for year, value in topp_aar], [value for year, value in topp_aar], 'ro',
             label='Topper')  # 'ro' markerer med røde prikker

plt.xlabel('År')
plt.ylabel('Antall solflekker')
plt.title('Solflekkaktivitet per år')
plt.legend()
plt.show()
