'''
Dette programmet har to deler. Den første er en funksjon som legger sammen to
tall.
Den andre delen er en funksjon som teller antall av en bokstav i et ord, dette
oppgir brukeren med input.
'''

# Funksjonen adder tar inn to tall og returnerer summen av de
def adder(tall1,tall2):
    return tall1+tall2

# Jeg kaller på funksjonen to ganger og printer resultatet
print(f'5 pluss 10 er lik {adder(5,10)}.')
print(f'3 pluss 6 er lik {adder(3,6)}.')

# tellForekomst itererer gjennom minTekst og sjekker om hver bokstav er lik minBokstav
def tellForekomst(minTekst,minBokstav):
    antall = 0
    for elm in minTekst:
        if elm is minBokstav:
            antall += 1
    return antall

# sjekkStr lar brukerern kun skrive inn bokstaver
def sjekkStr(inp):
    while inp.isalpha() == False:
        inp = input("Kun bokstaver: ")
    return inp

#Sjekker at bokstaven brukeren skriver inn er
def sjekkLen(inp):
    inp = sjekkStr(inp)
    while len(inp)!= 1:
        inp = sjekkStr(input("Skriv inn EN bokstav: "))
    return inp

# brukeren blir bedt om å skrive inn et ord og en bokstav, desse blir sjekka
ord = sjekkStr(input("Skriv inn et ord: "))
bokstav = sjekkLen(input("Skriv inn en bokstav: "))

# til slutt printes antallet av den gitte bokstaven i det gitte ordet.
print(tellForekomst(ord,bokstav))
