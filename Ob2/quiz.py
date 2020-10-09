'''
1. Lag et quiz der brukeren skal svare på en rekke spørsmål, kall programmet
quiz.py.

2. Lag variablen 'fasit' og gi den verdien til det som er rett svar,
lag variablen 'svar' og be brukeren svare på et spørsmål.

3. Lag en if/else-setning for å sjekke om brukeren har svart rett svar og print
om det var rett eller feil svar i terminalen.

4. Utvid programmet med å lage en metode 'kontroll' for å bruke if/else testen
for flere quiz spørsmål. Lag flere spørsmål til quizen.

5. Valgfritt: Utvid programmet til å telle rett og feil svar og gi brukeren
tilbakemelding med sitt resultat på slutten av quizen.
'''

#variablene rettSvar og feilSvar holder tellinga på antall rette og feil svar
rettSvar = 0
feilSvar = 0
#metoden kontroll sjekker svar mot fasit
def kontroll():
    #viss svaret er rett blir "Helt riktig!" printa og
    #variablen rettSvar øker med 1
    if svar == fasit:
        print("Helt riktig!")
        global rettSvar
        rettSvar += 1
    #viss svaret er feil blir "Det er feil" printa og
    #variablen feilSvar øker med 1
    else:
        print("Det er feil.")
        global feilSvar
        feilSvar += 1

#Spørsmål 1
svar = input("Hva er hovedstaden i Brasil?\n>").lower()
fasit = "brasilia"
kontroll()
#Spørsmål 2
svar = input("Hva er verdens lengste elv? \n>").lower()
fasit = "nilen"
kontroll()
#Spørsmål 3
svar = input("Hva er verdens raskeste dyr? \n").lower()
fasit = "gepard"
kontroll()
#Spørsmål 4
svar = input("I hvilket land ligger Niagara Falls? \n").lower()
fasit = "canada"
kontroll()

#utregning av resultatet av quizen
score = rettSvar/(rettSvar+feilSvar)
print(f'Feil svar: {feilSvar:10}')
print(f'Rett svar: {rettSvar:10}')
print(f'Score:{score:16.0%}')

#if setningen printer en helsing basert på scoren
if score < 0.25:
    print('Såpass ja...')
elif score > 0.75:
    print('Dayum son!')
else:
    print("Du klarer vel bedre?")
