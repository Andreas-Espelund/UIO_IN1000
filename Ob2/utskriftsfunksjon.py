'''
Metoden utskrift lagrer brukerens navn og stedet de kommer fra i variablene
'navn' og 'sted' ved hjelp av input. Deretter printar den en hilsen til brukeren
som inneholder de variablene. Den printer også en tom linje for å gjøre det
lttere å lese for brukeren.
'''
def utskrift():
    navn = input("Skriv inn ditt navn: ").capitalize()
    sted = input("Hvor kommer du fra? ").capitalize()
    print(f'Hei {navn}! Du er fra {sted}.')
    print()

'''
Jeg bruker en for løkke for å utføre metoden utskrift 3 ganger ved å bruke
variablen count. Denne får verdien 0, og øker med 1 hver gang for løkken
blir kjørt.
'''
i = 0
for i in range(3):
    utskrift()
    i += 1
