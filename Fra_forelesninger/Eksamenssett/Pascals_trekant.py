antall_linjer = int(input("Skriv inn antall linjer av Pascal's Trekant: "))

if antall_linjer > 0:
    print("[1]")

if antall_linjer > 1:
    print("[1, 1]")

forrige_linje = [1, 1]
for i in range(2, antall_linjer):
    nv_linje = [1]
    for i in range(1, len(forrige_linje)):
        nv_linje.append(forrige_linje[i] + forrige_linje[i-1])
    nv_linje.append(1)
    print(nv_linje)
    forrige_linje = nv_linje
