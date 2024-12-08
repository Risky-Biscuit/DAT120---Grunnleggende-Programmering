antall_rom = int(input("Antall rom: "))

total_areal = 0

for i in range(antall_rom):
    lengde = float(input("Lengden til rommet: "))
    bredde = float(input("Bredden til rommet: "))
    total_areal += lengde*bredde

print(f"Arealet ble: {total_areal}")


arealene = list()
for i in range(antall_rom):
    lengde = float(input("Lengden til rommet: "))
    bredde = float(input("Bredden til rommet: "))
    arealene.append(lengde*bredde)

total_areal = sum(arealene)
print(f"Arealet ble: {total_areal}")
