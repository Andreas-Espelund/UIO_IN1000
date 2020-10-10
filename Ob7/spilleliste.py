'''
Klassedefinisjon for Spilleliste

Klassen har instansvariablene _sanger og _navn
Klassens metoder er: lesFraFil, leggTilSanger,fjernSang,
fjernSang,finnSang,spillSang,spillAlle,hentArtistUtvalg.
'''

#jeg importerer klassen Sang
from sang import Sang

class Spilleliste:
    #Spilleliste-objektene blir initialistert med _navn og _sanger, som er en tom liste.
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn
    
    #__str__ funksjonen returnerer self._navn og self._sanger
    def __str__(self):
        output = self._navn+" :"+self._sanger
        return output

    #lesFraFIl tar et filnavn som parameter og leser inn linjene med artistnavn og tittel
    def lesFraFil(self,filnavn):
        sanger ={}
        i = 0
        fil = open(filnavn)
        #for hver linje i filen lager jeg et nytt Sang-objekt og legger det til spillelisten
        for linje in fil:
            biter = linje.split(";")
            tittel = biter[0]
            artist = biter[1].strip("\n")
            sanger[i] = Sang(tittel,artist)
            self.leggTilSang(sanger[i])
            i += 1
   
    #leggTilSang tar et Sang-objekt som parameter og legger det til i spillelisten
    def leggTilSang(self,sang):
        self._sanger.append(sang)
  
    #fjernSang tar et Sang-objekt som parameter og fjerner det fra spillelisten
    def fjernSang(self,sang):
        self._sanger.remove(sang)

    #finnSang tar en sangtittel som parameter og returnerer sangen dersom den er i spillelisten,
    #om den ikke er i listen returneres None
    def finnSang(self,tittel):
        for sang in self._sanger:
            if sang.sjekkTittel(tittel):
                return sang

    #spillSang bruker __str__ metoden til Sang objektet for å printe det til terminalen
    def spillSang(self,sang):
        print(sang)

    #spillAlle printer alle sangene
    def spillAlle(self):
        for sang in self._sanger:
            print(sang)

    #hentArtistUtvalg tar et artistNavn som parameter og lager en ny liste med alle
    #sangene til den artisten som er i spillelisten og returnerer den
    def hentArtistUtvalg(self,artistNavn):
        nySangliste=[]
        for sang in self._sanger:
            if sang.sjekkArtist(artistNavn):
                nySangliste.append(sang)
        return nySangliste
