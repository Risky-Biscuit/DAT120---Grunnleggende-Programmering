"""
Datetime er en klasse i Python som brukes til å håndtere dato og tid.
Det benytter seg av det internasjonale formate: Year, Month, Day, Hour, Minute, Seconds
"""

import datetime
print(datetime.datetime.now())

naa = datetime.datetime.now()

et_tidspunkt = datetime.datetime(2024, 3, 5, 12, 15, 00)
print(et_tidspunkt)

et_tidspunkt_til = datetime.datetime(2023, 9, 23)
print(et_tidspunkt_til)

# Tidspunktene kan sammenlignes
print(et_tidspunkt > et_tidspunkt_til)
print(et_tidspunkt < et_tidspunkt_til)

# Vi kan også hente ut gitte tidspunkt som måneden, året, minuttet osv.
print(et_tidspunkt.year)
print(et_tidspunkt.month)
print(et_tidspunkt.day)
print(et_tidspunkt.hour)
print(et_tidspunkt.minute)
print(et_tidspunkt.second)
