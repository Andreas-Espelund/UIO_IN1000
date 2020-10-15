'''
Dette programmet har flere programmer som utfører ulike matematiske beregninger.
Brukeren oppgir tall som blir beregnet i disse funksjonene og printer de til terminalen.
'''

#addisjon tar to tall som parameter og returnerer summen av tallene
def addisjon(tall1,tall2):
    return tall1+tall2

#jeg kaller på funksjonen addisjon med 5 og 7 som argument og printer resultatet
print("5 + 7 =",addisjon(5,7))

#subtraksjon tar to tall som parameter og returnerer differansen
def subtraksjon(tall1,tall2):
    return tall1-tall2

#divisjon tar to tall som parameter og returnerer kvotienten
def divisjon(tall1,tall2):
    return tall1/tall2

#assert uttrykk for addisjon
assert addisjon(1,2) == 3
assert addisjon(-1,5) == 4
assert addisjon(-1,-2) == -3

#assert uttrykk for subtraksjon
assert subtraksjon(5,1) == 4
assert subtraksjon(5,-1) == 6
assert subtraksjon(-5,-1) == -4

#assert uttrykk for divisjon
assert divisjon(6,2) == 3
assert divisjon(2,-2) == -1
assert divisjon(-4,-2) == 2

#tommerTilCm tar antall tommer som parameter og returnerer verdien i cm.
def tommerTilCm(antallTommer):
    assert antallTommer > 0
    centimeter = antallTommer*2.54
    return centimeter

#assert uttrykk for tommerTilCm
assert tommerTilCm(1) == 2.54
assert tommerTilCm(2) == 5.08
assert tommerTilCm(10) == 25.4

#sjekktall lar brukeren skrive inn flyttal eller heltall
def sjekkTall(inp):
    while True:
        try:
            inp = float(inp)
        except:
            inp = input("Skriv inn TALL:")
        else:
            return inp

#skrivBeregninger ber om tall som input og utfører addisjon,subtraksjon,divisjon
#så tar den et nytt tall og gjør det om fra tommer til centimeter
def skrivBeregninger():
    print("Utregninger:")
    tall1 = float(sjekkTall(input("Skriv inn tall 1: ")))
    tall2 = float(sjekkTall(input("Skriv inn tall 2: ")))
    print(f'Resultatet av addisjonen er: {addisjon(tall1,tall2)}')
    print(f'Restultatet av subtraksjonen er: {subtraksjon(tall1,tall2)}')
    print(f'Resultatet av divisjonen er: {divisjon(tall1,tall2):.2f}')
    print("")
    print("Konvertering fra tommer til cm:")
    tommer = float(sjekkTall(input("Skriv inn et tall (tommer): ")))
    print(f'{tommer} tommer er {tommerTilCm(tommer):.2f} cm.')

#jeg kaller på skrivBeregninger
skrivBeregninger()
