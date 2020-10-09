'''
testMotorsykkel tester klassen Motorsykkel ved å opprette objekter av denne klassen 
'''

# jeg importerer klassen Motorsykkel fra filen motorsykkel.py
from motorsykkel import Motorsykkel

def hovedprogram():
    #jeg lager 3 objekter av klassen Motorsykkel og gir de
    #merke, registreringsnummer og kilometerstand.
    honda = Motorsykkel("Honda","UF3219",7543)
    yamaha = Motorsykkel("Yamaha","BA1542",3254)
    jawa = Motorsykkel("Jawa","JJ1015",16788)

    #jeg kaller på .skrivUt() metodene for alle objektene
    honda.skrivUt()
    yamaha.skrivUt()
    jawa.skrivUt()
    #jeg kaller på .kjor() metoden for jawa motorsykkelen
    jawa.kjor(10)
    #så printer jeg kilometerstanden til jawa-en, som nå har gått opp med 10km.
    print("Kilometerstand for Jawa-en er ",jawa.hentKilometerstand(),"km")

#kall på hovedprogram
hovedprogram()
