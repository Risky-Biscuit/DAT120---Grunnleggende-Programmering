import turtle

antall_sekskanter = int(input("Hvor mange sekskanter ønsker du? "))

# Sett opp skilpadden
turtle.color("Black")
turtle.speed(3)
turtle.pensize(2)

# Flytt skilpadden opp på skjermen for å få mer plass
turtle.penup()      # løft pennen
turtle.left(90)     # Roter 90 grader til venstre
turtle.forward(300) # Går frem 300 piksler
turtle.right(90)    # Roter 90 grader til høyre

# Tegn en sekskant med en for-løkke hvis antall blir satt til 1
if antall_sekskanter == 1:
    for _ in range(6):
        turtle.pendown()    # Sett ned pennen
        turtle.forward(80)  # Gå frem 80 piksler
        turtle.right(60)    # Roter 60 grader til høyre


if antall_sekskanter > 1:
    turtle.pendown()  # Sett ned pennen
    for _ in range(6):
        turtle.forward(80)  # Gå frem 80 piksler
        turtle.right(60)  # Roter 60 grader til høyre
    turtle.penup()
    turtle.right(120)
    turtle.forward(80)
    turtle.left(60)
    turtle.forward(80)
    turtle.left(60)
    turtle.forward(80)
    turtle.pendown()
    for x in range(antall_sekskanter - 1):
        turtle.right(60)
        turtle.forward(80)
        turtle.right(60)
        turtle.forward(80)
        turtle.right(60)
        turtle.forward(80)
        turtle.right(60)
        turtle.forward(80)
        turtle.right(60)
        turtle.forward(80)
        turtle.right(60)
        turtle.forward(80)
        turtle.right(60)
        turtle.forward(80)
        turtle.right(60)
        turtle.forward(80)
        turtle.left(120)



turtle.done()
