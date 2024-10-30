from math import *
def f(x):
    return sin(x**2)

n=int(input("Hva er n? ")) # Antallet steg det skal brukes
a=float(input("Intervall start: ")) #Intervallet det skal integreres over [a,b]
b=float(input("Intervall slutt: "))
deltax=(b-a)/n #Definerer Steglengde
x=a
T=0

for i in range(n): # Bruker 'for'-løkke i fra 0 til n-1
    T=T+(f(x)+4*f(x+deltax/2)+f(x+deltax))*deltax/6 #Bruker Simpsons regel for hvert delintervall
    x=x+deltax

print("Integralets verdi er", round(T,8))
