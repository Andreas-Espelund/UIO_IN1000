'''
Klassedefinisjon for Spillebrett-ojekter

Klassen har metodene:
    * finnNabo
    * oppdatering
    * _generer
    * tegnBrett
    * finnAntallLevende
    * lagStatestikk
    * lagProsentBar
'''

# eg importerer random og klassen Celle
import random
from celle import Celle

#Spillebrett objekter blir initisert med antall rader og kolonner
#Det faar også en instansvariabel for kva generasjon brettet er på, den starter som 0
class Spillebrett:
    def __init__(self,rader,kolonner):
        self._rader = rader #horisontal
        self._kolonner = kolonner #vertikal
        self._generasjon = 0

        #eg la til en instansvariabel for totalt antall celler paa brettet for aa
        #kunne lage meir statesikk for spillebrettet
        self._antallCeller = rader*kolonner

        #det blir laget et rutenett som er en nostet liste med 'kolonner' antall
        #lister som hver inneholder 'rader' antall celle-objekter
        self._rutenett = []
        for i in range(self._kolonner):
            rad = []
            for j in range(self._rader):
                nyCelle = Celle()
                rad.append(nyCelle)
            self._rutenett.append(rad)


        #kall på _generer metoden for å klargjere et tilfeldig spillebrett
        self._generer()



    #_generer itererer gjennom rutenettet og har en 1/3 sjanse
    #for å endre en celle til levende
    def _generer(self):
        for rad in self._rutenett:
            for celle in rad:
                if random.randint(0,2) == 1:
                    celle.settLevende()



    #instansmetoden finnNabo tar et celle-objekt sin plassering i rutenettet og
    #returnerer en liste med de tilstøtende celle-objektene (naboene)
    def finnNabo(self,rad,kolonne):
        #jg ser på rad og kolonne som koordinater på et kart
        #mainX og mainY, er hovedcellen sine koordinater
        mainX = rad
        mainY = kolonne
        naboer = []

        #eg iterer gjennom alle cellene i rutenettet og legger cellen til
        #naboer dersom den har en tilstøtende koorinat
        y=0
        for rad in self._rutenett:
            x = 0

            for elm in rad:
                #her kunne eg brukt and istedenfor to ekstra if setningar,
                if (x==mainX) or (x==mainX+1) or (x==mainX-1):
                    if (y==mainY) or (y==mainY+1) or(y==mainY-1):
                        if not ((x==mainX) and (y==mainY)):
                            naboer.append(elm)

                x += 1
            y += 1

        return naboer


    #oppdatering sjekker utifra spillets regler kva celler som skal leve eller doe,
    #disse cellene som skal skifte status blir lagt til i den aktuelle listen
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


    #tegnBrett tommer skjermen, saa printer den alle cellene i rutenettet
    def tegnBrett(self):
        #tom skjerm, 100 blanke linjer
        for i in range(100):
            print("")

        #for-lokken skriver ut rutenettet i et pent format
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


    #jeg la til en prosedyre som lager en prosent-bar som gjør det lett
    #å se hvor stor andel av cellene som er levende
    def lagProsentBar(self):
        #eg reknar ut prosent levande celler
        levende = self.finnAntallLevende()
        prosent = int(levende/self._antallCeller*100)
        prosentStr = (str(prosent)+"%")

        #prosentbaren bestaar av en fyll streng og en tom streng
        fyll = "█"*int(prosent/2)
        tom = " "*(49-int(prosent/2))

        #her printes prosentbaren med en ramme rund med tittel og prosent
        print("-"*22,"Levende","-"*23)
        print("|",fyll,tom,"|")
        print("-"*24,prosentStr,"-"*(28-len(prosentStr)))
