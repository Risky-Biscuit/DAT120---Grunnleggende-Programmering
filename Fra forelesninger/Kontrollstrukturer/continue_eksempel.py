"""
En overtroisk byggleder har bedt om at hans nye bygning ikke skal ha en 13. etajse...
"""

for etasje in range(1, 20):
    if etasje == 13:
        continue
    print(f"Etasjenummer: {etasje:2d}")
