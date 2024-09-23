filreferanse = open("En_tekstfil", "r", encoding="utf-8")
for linje in filreferanse:
    print(linje)
filreferanse.close()
