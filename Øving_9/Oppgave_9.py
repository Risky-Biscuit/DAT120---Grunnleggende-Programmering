"""
Lag en klasse «Maalinger_aar». Hvert objekt av denne klassen representerer de dataene
dere trenger for å plotte ett enkelt år. Dere skal legge til alle målinger for et bestemt år i
Maalinger_aar objektet for det året. Klassen Maalinger_aar skal ha egenskapene år,
total_solflekker, antall_målinger, maks_daglig og min_daglig.
a. Konstruktøren til klassen skal ta år som parameter og sette egenskapen år lik det
oppgitte året. Gi de andre egenskapene verdier som gir mening for et tomt objekt
som ikke enda lagrer noen målinger.
b. Lag en metode for å sette inn en ny måling. Metoden skal ta antall solflekker den
dagen som parameter. Metoden skal legge dette til totalen, legge 1 til antallet, og
oppdatere maks og min om nødvendig.
c. Lag en metode for å hente ut gjennomsnittlig antall solflekker. Gjennomsnittet er
total delt på antall.
"""

import matplotlib.pyplot as plt


class Maalinger_aar:
    def __init__(self, aar):
        self.aar = aar
        self.total_solflekker = 0
        self.antall_maalinger = 0
        self.maks_daglig = 0
        self.min_daglig = 1000000

    def ny_maaling(self, antall_solflekker):
        self.total_solflekker += antall_solflekker
        self.antall_maalinger += 1
        if antall_solflekker > self.maks_daglig:
            self.maks_daglig = antall_solflekker
        if antall_solflekker < self.min_daglig:
            self.min_daglig = antall_solflekker

    def gjennomsnittlig_solflekker(self):
        return self.total_solflekker / self.antall_maalinger

"""
I hovedprogrammet (if __name__ == «__main__» blokken), lag et dictionary som har år
som nøkkel og et tomt Maaling objekt for det året som verdi
"""

#if __name__ == "__main__":
maalinger = {}

"""
Lag kode som leser inn fila. Format på solflekk-fila er: år; måned; dag; år-milliår; antall
solflekker; standardavvik mellom observasjonene den dagen; antall observasjoner den
dagen; om dette er en endelig eller midlertidig verdi. -1 for antall solflekker betyr at det
mangler data for den dagen, disse linjene kan du bare hoppe over. I denne oppgaven skal
du bare bruke kolonnene år og antall solflekker
"""

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


"""
Plott resultatet. Du må da gå gjennom dictionariet med maaling-objekter og lag de
nødvendige listene og deretter plotte dette med matplotlib
"""

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

# Opprett plottet
plt.figure(figsize=(10, 6))
plt.plot(years, average_solflekker, label='Gjennomsnitt', color="black")
plt.plot(years, max_solflekker, label='Maksimum', color="orange", linestyle="dashed")
plt.plot(years, min_solflekker, label='Minimum', color="blue", linestyle="dashed")
plt.xlabel('År')
plt.ylabel('Antall solflekker')
plt.title('Solflekkaktivitet per år')
plt.legend()
plt.show()
