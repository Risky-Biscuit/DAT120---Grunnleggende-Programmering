#def test():
 #   testen = (input("Kan du gjøre dette? "))
  #  print(testen)
   # return testen


#testen = test()







#ef hils(navn):  # 'navn' er en parameter
 #   print("Hei, " + navn + "!")  # Her bruker vi parameteren

#navn = input("Hva er navnet ditt? ")

#hils(navn)  # Vi kaller funksjonen og sender inn "Ola" som et argument


#import math


#def løs_andregradslikning():
    # Be om brukerinput for a, b, og c
   # a = float(input("Verdi for a: "))
  #  b = float(input("Verdi for b: "))
 #   c = float(input("Verdi for c: "))

    # Beregn diskriminanten
#    diskriminant = b ** 2 - 4 * a * c

    # Sjekk om diskriminanten er negativ, null, eller positiv
    #if diskriminant > 0:
        #x1 = (-b + math.sqrt(diskriminant)) / (2 * a)
       # x2 = (-b - math.sqrt(diskriminant)) / (2 * a)
      #  print(f"Likningen har to løsninger: x1 = {x1} og x2 = {x2}")
     #   return x1, x2
    #elif diskriminant == 0:
      #  x = -b / (2 * a)
     #   print(f"Likningen har én løsning: x = {x}")
    #    return x
   # else:
  #      print("Likningen har ingen reelle løsninger.")
 #       return None


# Kall funksjonen og lagre resultatet i en variabel
#løsninger = løs_andregradslikning()

# Nå kan du bruke 'løsninger' videre i koden om nødvendig


import turtle

def tegn_sekskant(sidelengde):
    # Funksjonen tegner en sekskant med gitt sidelengde
    for i in range(6):
        turtle.forward(sidelengde)
        turtle.left(60)

# Funksjon for å flytte skilpadden til en ny posisjon uten å tegne
def flytt_til(x, y):
    turtle.penup()  # Løft pennen opp
    turtle.goto(x, y)  # Flytt til (x, y)-posisjonen
    turtle.pendown()  # Sett pennen ned igjen

# Sett opp skilpadden
turtle.color("blue")
turtle.pensize(2)
turtle.speed(3)

# Tegn fire sekskanter på ulike steder med ulik størrelse
flytt_til(-100, 100)  # Flytt til øvre venstre hjørne
tegn_sekskant(50)     # Tegn en sekskant med sidelengde 50

flytt_til(100, 100)   # Flytt til øvre høyre hjørne
tegn_sekskant(70)     # Tegn en sekskant med sidelengde 70

flytt_til(-100, -100) # Flytt til nedre venstre hjørne
tegn_sekskant(90)     # Tegn en sekskant med sidelengde 90

flytt_til(100, -120)  # Flytt til nedre høyre hjørne
tegn_sekskant(120)    # Tegn en sekskant med sidelengde 120

# Fullfør tegningen
turtle.done()
