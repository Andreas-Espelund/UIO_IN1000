'''
Klassedefinisjon for Spilleliste

Klassen har instansvariablene _sanger og _navn
Klassens metoder er: lesFraFil, leggTilSanger,fjernSang,
fjernSang,finnSang,spillSang,spillAlle,hentArtistUtvalg.
'''

#eg importerar klassa Sang
from sang import Sang

class Spilleliste:
    #Spilleliste-objekta blir initialistert med _navn og _sanger, som er ei tom liste.
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    #__str__ funksjonen returnerar self._navn og self._sanger
    def __str__(self):
        output = self._navn+" :"+self._sanger
        return output

    #lesFraFIl tar eit filnavn som parameter og les inn linjene med artistnavn og tittel
    def lesFraFil(self,filnavn):
        sanger ={}
        i = 0
        fil = open(filnavn)
        #for kvar linje i fila lagar eg eit nytt Sang-objekt og legg det til i  spelelista
        for linje in fil:
            biter = linje.split(";")
            tittel = biter[0]
            artist = biter[1].strip("\n")
            sanger[i] = Sang(artist,tittel,None)
            self.leggTilSang(sanger[i])
            i += 1

    #leggTilSang tar eit Sang-objekt som parameter og legg det til i spelelista
    def leggTilSang(self,sang):
        self._sanger.append(sang)

    #fjernSang tar eit Sang-objekt som parameter og fjernar det frå spelelista
    def fjernSang(self,sang):
        self._sanger.remove(sang)

    #finnSang tar ein sangtittel som parameter og returnerer sangen dersom den er i spelelista,
    #om den ikkje er i lista returneres None
    def finnSang(self,tittel):
        for sang in self._sanger:
            if sang.sjekkTittel(tittel):
                return sang

    #spillSang bruker __str__ metoden til Sang objektet for å printe objektet det til terminalen
    def spillSang(self,sang):
        print(sang)

    #spillAlle printar alle sangene
    def spillAlle(self):
        for sang in self._sanger:
            sang.spill()

    #hentArtistUtvalg tar eit artistNavn som parameter og lagar ein ny liste med alle
    #sangene til den artisten, som er i spelelista, og returnerar den.
    def hentArtistUtvalg(self,artistNavn):
        nySangliste=[]
        for sang in self._sanger:
            if sang.sjekkArtist(artistNavn):
                nySangliste.append(sang)
        return nySangliste
