import turtle

# Sett opp skilpadden
turtle.color("blue")
turtle.pensize(3)
turtle.speed(3)

# Tegn en sekskant med en for-løkke
for _ in range(6):
    turtle.forward(80)  # Gå frem 80 piksler
    turtle.right(60)    # Roter 60 grader til høyre

# Fullfør tegningen
turtle.done()
