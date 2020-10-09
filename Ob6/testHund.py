'''
Dette programmet tester klassen Hund ved å lage et objekt av denne klassen og kalle
på klassens instansvariabler.
'''

#jeg importerer klassen Hund fra filen hund
from hund import Hund

#jeg legger alle funksjonskallene i hovedprograms
def hovedprogram():
    #jeg lager et Hund-objekt med alder 5 og vekt 20 og kaller den doge
    doge = Hund(5,20)

    #løkken kaller på instansmetodene spring og spis to ganger,
    #for så å skrive ut vekten med .hentVekt()
    for i in range(2):
        print("")
        doge.spring()
        doge.spis(1+i*3) #hunden spiser først 3 porsjoner, så 4
        print("Hundens vekt er nå",doge.hentVekt(),"kg")


#kall på hovedprogram
hovedprogram()
