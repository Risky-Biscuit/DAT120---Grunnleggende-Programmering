"""
Lag et program som bruker turtle graphics tegner ut en serie diamanter (kvadrater som er rotert 45
grader i forhold til horisontalen), den ene utenfor den andre. Brukeren skal angi hvor mange
diamanter den skal tegne opp. Figurene under viser hva den skal tegne opp for 3 og 5 diamanter.
Husk: For å løse dette, tenk over hvilke delproblemer du trenger å løse og løs deretter hvert
delproblem for seg. Tegn et flytskjema og/eller skriv en algoritme som punktliste før du starter å
programmere
"""
import turtle

# Ber bruker om input for antall diamanter som skal tegnes
antall_diamanter = int(input("Hvor mange diamanter skal vi tegne? "))

# Setter en størrelse til å starte med og et increment jeg ønsker å bruke som utgangspunkt til å øke størrelsen
# på diamantene
base_size = 50
increment = 70

# Begynner å tegne diamantene
turtle.penup()
for y in range(antall_diamanter):
    current_size = base_size + y*increment
    turtle.forward(50)
    turtle.left(135)
    for x in range(4):
        turtle.pendown()
        turtle.forward(current_size)
        turtle.left(90)
    turtle.right(135)
    turtle.penup()
turtle.done()
