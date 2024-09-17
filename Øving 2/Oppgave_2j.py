import turtle

kanter = int(input("Hvor mange kanter ønsker du? "))
vinkel = 360 / kanter

# Sett opp skjermen
skjerm = turtle.Screen()
skjerm.bgcolor("white")

# Sett opp skilpadden
skilpadde = turtle.Turtle()
skilpadde.color("black")
skilpadde.pensize(2)
skilpadde.speed(3)

# Tegn en mangekant med en for-løkke
for _ in range(kanter):
    skilpadde.forward(80)  # Gå frem 80 piksler
    skilpadde.right(vinkel)    # Roter så mange grader som trengs til høyre

# Fullfør tegningen
turtle.done()
