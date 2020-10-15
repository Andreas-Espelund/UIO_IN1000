'''
Jeg lagrer datoen i to variabler, en for dag og en for måned.
Jeg bruker int() for å gjøre brukerinput om til heltall.
'''
print("Dato 1:")
dato1d = int(input("Skriv inn en dag (DD): "))
dato1m = int(input("Skriv inn måned (MM):"))

print("Dato 2:")
dato2d = int(input("Skriv inn en dag (DD): "))
dato2m = int(input("Skriv inn måned (MM): "))
'''
IF testen sjekker først at rekkefølgen på månedene er riktig
Viss det er sant, blir "Riktig rekkefølge" printa til terminalen.
'''
if dato1m<dato2m or (dato1m==dato2m and dato1d<dato2d):
    print("Riktig rekkefølge")
#Viss IF setninga ikke er sann, sjekker elif om rekkefølgen på dagene er rett
elif dato1m>dato2m or (dato1m==dato2m and dato1d>dato2d):
    print("Feil rekkefølge")
#Viss elif setninga ikke er sann, betyr det at datoene er like
#Og "Samme dato!" blir printa til terminalen.
else:
    print("Samme dato!")
