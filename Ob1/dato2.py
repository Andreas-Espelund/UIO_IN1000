'''
Her hentar eg inn datoen som en streng og lagar to variablar
datoen blir lagra i to variablar, en for dag og en for måned
Eg hentar ut dei to siste siffera for måneden og dei to første for dagen.
Eg brukar int() for å formatere variablane som heiltall
'''
dato1 = input("Skriv inn dato (DDMM):")
dato1m = int(dato1[2:4])
dato1d = int(dato1[0:2])

dato2 = input("Skriv inn dato (DDMM):")
dato2m = int(dato2[2:4])
dato2d = int(dato2[0:2])

'''
IF testen sjekkar først at rekkefølga på månedane er riktig
Dersom det er sant, blir "Riktig rekkefølge" printa til terminalen.
'''
if dato1m<dato2m or (dato1m==dato2m and dato1d<dato2d):
    print("Riktig rekkefølge")
#Dersom IF setninga ikkje var sann, sjekkar elif om rekkefølga på dagane er rett
elif dato1m>dato2m or (dato1m==dato2m and dato1d>dato2d):
    print("Feil rekkefølge")
#Dersom elif setninga ikkje er sann, betyr det at datoane er like
#Og "Samme dato!" blir printa til terminalen.
else:
    print("Samme dato!")
