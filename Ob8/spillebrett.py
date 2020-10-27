'''
Klassedefinisjon for Spillebrett-ojekter

Klassen har metodene:
    * finnNabo
    * oppdatering
    * _generer
    * tegnBrett
    * finnAntallLevende
    * lagStatestikk
'''

# jeg importerer random og klassen Celle
import random
from celle import Celle

#Spillebrett objekter blir initisert med antall rader og kolonner
#De faar også en instansvariabel for hvilken generasjon brettet er på, den starter som 0
class Spillebrett:
    def __init__(self,rader,kolonner):
        self._rader = rader #horisontal
        self._kolonner = kolonner #vertikal
        self._generasjon = 0

        #det blir laget et rutenett som er en nostet liste med 'kolonner' antall
        #lister som hver inneholder 'rader' antall celle-objekter
        self._rutenett = []
        for i in range(self._kolonner):
            rad = []
            for j in range(self._rader):
                nyCelle = Celle()
                rad.append(nyCelle)
            self._rutenett.append(rad)


        #kall på _generer metoden for å klargjøre et tilfeldig spillebrett
        self._generer()

    #instansmetoden finnNabo tar et celle-objekt sin plassering i rutenettet og
    #returnerer en liste med de tilstøtende celle-objektene (naboene)
    def finnNabo(self,rad,kolonne):
        #jeg ser på rad og kolonne som koordinater på et kart
        #mainX og mainY, er hovedcellen sine koordinater
        mainX = rad
        mainY = kolonne
        naboer = []

        #jeg iterer gjennom alle cellene i rutenettet og legger cellen til
        #naboer dersom den har en tilstøtende koorinat
        y=0
        for rad in self._rutenett:
            x = 0
            for elm in rad:
                if (x==mainX) or (x==mainX+1) or (x==mainX-1):
                    if (y==mainY) or (y==mainY+1) or(y==mainY-1):
                        if not ((x==mainX) and (y==mainY)):
                            naboer.append(elm)

                x += 1
            y += 1

        return naboer

    #oppdatering sjekker utifra spillets regler hvike celler som skal leve eller dø,
    #disse cellene som skal skifte status blir lag til i den aktuelle listen
    def oppdatering(self):

        skalLeve = []
        skalDoe = []

        y=0
        for rad in self._rutenett:
            x = 0
            for celle in rad:

                naboer = self.finnNabo(x,y)
                levendeNaboer = 0
                for nabo in naboer:
                    if nabo.erLevende():
                        levendeNaboer += 1

                if celle.erLevende():
                    if (levendeNaboer > 3) or (levendeNaboer < 2):
                        skalDoe.append(celle)
                else:
                    if levendeNaboer == 3:
                        skalLeve.append(celle)

                x += 1
            y += 1

        #til slutt kalles settLevende eller settDoed for celleobjektene
        for celle in skalLeve:
            celle.settLevende()

        for celle in skalDoe:
            celle.settDoed()

        #jeg oker generasjon telleren med 1
        self._generasjon += 1


    #_generer itererer gjennom rutenettet og har en 1/3 sjanse
    #for å endre en celle til levende
    def _generer(self):
        for rad in self._rutenett:
            for celle in rad:
                if random.randint(0,2) == 1:
                    celle.settLevende()

    #tegnBrett tommer skjermen, saa printer den alle cellene i rutenettet
    def tegnBrett(self):
        #tom skjerm
        for i in range(100):
            print("")

        for rad in self._rutenett:
            for celle in rad:
                print(celle, end="")
            print("")

    #finnAntallLevende returnerer antall levende celler paa spillebrettet
    def finnAntallLevende(self):
        levende = 0

        for rad in self._rutenett:
            for celle in rad:
                if celle.erLevende():
                    levende +=1

        return levende

    #lagStatestikk returnerer en streng som inneholder info om generasjon og
    #antall levende celler
    def lagStatestikk(self):
        levende = self.finnAntallLevende()

        return "Generasjon: "+str(self._generasjon)+" - "+"Antall levende celler: "+str(levende)
