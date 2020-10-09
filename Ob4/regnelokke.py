'''
Dette programmet lager en liste med tall som brukeren skriver inn.
Denne listen blir printen, summert og jeg finner det største og minste
tallet i listen.
'''

# sjekkTall lar brukeren kun skrive inn tall
def sjekkTall(num):
    while num.isdigit() == False:
        num= input("Skriv inn et tall (ingen bokstaver!): ")
    num = int(num)
    return num


liste = []

# while løkken tar et tall sjekker om det er 0, viss ikke legger det til listen
# dersom brukeren skriver inn 0, blir det ikke lagt til i listen og løkken er ferdig.
ferdig = False
while ferdig == False:
    tall = sjekkTall(input("Skriv inn et tall: "))
    if tall == 0:
        ferdig = True
    else:
        liste.append(tall)

# for løkka skriver ut alle elementene i listen
for num in liste:
    print(num)

# denne løkken legger sammen alle tallene i listen og skriver de ut
minSum = 0
for num in liste:
    minSum = minSum + num

print(f'Summen av de oppgitte tallene er {minSum}')

# for å finne det minste tallet tar jeg utgangspunkt i det første tallet,
# så sjekker jeg med en for løkke alle tallene, dersom et tall er mindre enn
# minste, blir dette tallet til minste.
minste = liste[0]
for num in liste:
    if num < minste:
        minste = num

print(f'Det minste tallet i listen er {minste}')

# Her skjer det samme som i løkken ovenfor, bare med storste istedenfor minste
storste = liste[0]
for num in liste:
    if num > storste:
        storste = num

print(f'Det storste tallet i listen er {storste}')
