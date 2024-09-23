try:
    fil_inn = open("tallverdier", "r")
    fil_ut = open("tall_ut", "w")
    for linje in fil_inn:
        tall = float(linje)
        resultat = tall*1.1
       # fil_ut.write(str(resultat) + "\n")
        fil_ut.write(f"{resultat:.2f} \n")
except FileNotFoundError:
    print("Kunne ikke finne filen som skal leses.")
except ValueError:
    print("Filen har feil format.")
except IOError:
    print("Filen er skadet.")
finally:
    fil_inn.close()
    fil_ut.close()
