import numpy as np

"""
Funksjonen tar inn en liste med tider, en liste med temperaturer og et tall n.
For hvert gyldig tidspunkt regnes snittet av de n forrige målingene, den nåværende målingen og de n neste målingene.
Gyldige tidspunkter er alle tidspunkter hvor du ikke havner utenfor lista ved å gå n hakk bakover eller forover.
Funksjonen returnerer lister med gyldige tidspunkter og gjennomsnittsverdier.
"""
def stoy_reduksjon(tider: list, temperaturer: list, n: int):
    tidspunkter = list() # Lager en tom liste for tidspunkter
    gjennomsnittsverdier = list() # Lager en tom liste for gjennomsnittsverdier
    for i in range(len(temperaturer)): # Går gjennom alle temperaturer
        if i - n >= 0 and i + n < len(temperaturer): # Avgrenser til gyldige tidspunkter
            snitt = np.mean(temperaturer[i-n:i+n+1]) # Regner ut snittet av de n forrige målingene, den nåværende målingen og de n neste målingene
            tidspunkter.append(tider[i]) # Legger til tidspunktet i listen
            gjennomsnittsverdier.append(snitt) # Legger til snittet i listen
    return tidspunkter, gjennomsnittsverdier # Returnerer tidspunkter og gjennomsnittsverdier

# Lokal testkjøring av funksjonen med eksempeldata lokalt
if __name__ == "__main__":
    tider = ["11.06.2021 kl.17:31", "11.06.2021 kl.17:32", "11.06.2021 kl.17:33", "11.06.2021 kl.17:34", "11.06.2021 kl.17:35",
             "11.06.2021 kl.17:36", "11.06.2021 kl.17:37", "11.06.2021 kl.17:38", "11.06.2021 kl.17:39", "11.06.2021 kl.17:40"]
    temperaturer = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    n = 2
    tidspunkter, gjennomsnittsverdier = stoy_reduksjon(tider, temperaturer, n)
    print(tidspunkter)
    print(gjennomsnittsverdier)
    """
    Forventet output:
    ['11.06.2021 kl.17:33', '11.06.2021 kl.17:34', '11.06.2021 kl.17:35', '11.06.2021 kl.17:36', '11.06.2021 kl.17:37', '11.06.2021 kl.17:38']
    [14.0, 16.0, 18.0, 20.0, 22.0, 24.0]
    """

    # Plotting
    import matplotlib.pyplot as plt
    plt.plot(tider, temperaturer, label="Temperatur") # Plotter temperatur
    plt.plot(tidspunkter, gjennomsnittsverdier, label="Gjennomsnittstemperatur") # Plotter gjennomsnittstemperatur
    plt.xlabel("Tid") # Navn på x-akse
    plt.ylabel("Temperatur") # Navn på y-akse
    plt.legend() # Viser labelene
    plt.show() # Viser plottet







"""
from stoy_reduksjons_funksjon import stoy_reduksjon

# Beregn gjennomsnittet for hver tidsperiode ved hjelp av stoy_reduksjon-funksjonen
n = 30  # Antall verdier per gjennomsnitt
gjennomsnitt_tider, gjennomsnitt_temperaturer = stoy_reduksjon(datoarray2, temperaturarray2, n)

# Legg til gjennomsnittstemperaturene i plottet
plt.subplot(2, 1, 1)  # Oppretter et subplot til temperaturene og plotter dem
plt.ylabel("Temperatur")
plt.plot(datoarray1, temperaturarray1, color="green", label="Original Temperatur")
plt.plot(datoarray2, temperaturarray2, color="blue", label="Temperatur Blå")
plt.plot(gjennomsnitt_tider, gjennomsnitt_temperaturer, color='orange', label='Gjennomsnittstemperatur', linewidth=1)
plt.legend()

plt.subplot(2, 1, 2)  # Oppretter et subplot til trykkverdiene og plotter dem
plt.ylabel("Trykk hPa")
plt.xlabel("Tidspunkt")
plt.plot(datoarray1, lufttrykkarray1, color="green", label="Lufttrykk Grønn")
plt.plot(datoarray3, lufttrykkarray2, color="orange", label="Lufttrykk Oransje")
plt.plot(datoarray2, abstrykkarray, color="blue", label="Absolutttrykk Blå")
plt.legend()
plt.show()
"""
