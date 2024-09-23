tall = int(input("Opp til hvilket heltall ønsker du å se gangetabellen? "))

for b in range(1,tall+1):
    print()
    print(f"{b:2d}:", end="")
    for a in range(1, 11):
        print(f"{a*b:4d}", end="")
