from math import *
def f(x):
    return sin(x**2)

n=int(input("Hva er n? ")) # Antallet steg/trapes det skal brukes
a=float(input("Intervall start: ")) #Intervallet det skal integreres over [a,b]
b=float(input("Intervall slutt: "))

deltax=(b-a)/n #Definerer Steglengde
T=(f(a)+f(b))*deltax/(2) # Disse verdiene er annerledes, regner disse først
x=a

for i in range(n-1): # Bruker 'for'-løkke
    x=x+deltax
    T=T+f(x)*deltax


print("Integralets verdi er", round(T,8))
