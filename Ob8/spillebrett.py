'''
Klassedefinisjon for spillebrettet
'''

import random
from celle import Celle

class Spillebrett:
    def __init__(self,rader,kolonner):
        self._rader = rader #horisontal
        self._kolonner = kolonner #vertikal
        self._generasjon = 0

        self._rutenett = []
        for i in range(self._kolonner):
            rad = []
            for j in range(self._rader):
                nyCelle = Celle()
                rad.append(nyCelle)
            self._rutenett.append(rad)


        #initial seed
        self._generer()

    def finnNabo(self,rad,kolonne):
        mainX = rad
        mainY = kolonne
        naboer = []

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

        for celle in skalLeve:
            celle.settLevende()

        for celle in skalDoe:
            celle.settDoed()

        self._generasjon += 1


    def _generer(self):
        for rad in self._rutenett:
            for celle in rad:
                if random.randint(0,2) == 1:
                    celle.settLevende()


    def tegnBrett(self):
        #tom skjerm
        for i in range(100):
            print("")

        for rad in self._rutenett:
            for celle in rad:
                print(celle, end="")
            print("")

    def finnAntallLevende(self):
        levende = 0

        for rad in self._rutenett:
            for celle in rad:
                if celle.erLevende():
                    levende +=1

        return levende

    def lagStatestikk(self):
        levende = self.finnAntallLevende()

        return "Generasjon: "+str(self._generasjon)+" - "+"Antall levende celler: "+str(levende)
