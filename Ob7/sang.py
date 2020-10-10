'''
Klassedefinisjon for Sang:

Klassen har instansvariablene _tittel og _artist, og 
metodene spill, sjekkArtist, sjekkTittel og sjekkArtistOgTittel. 
'''

class Sang:
    #sang objektene blir initialisert med _artist og _tittel som instansvariabler
    def __init__(self,artist,tittel):
        self._tittel = tittel.lower()
        self._artist = artist.lower()
    #__str__ returnerer artistnavn og låtnavn på en lesbar måte
    def __str__(self):
        out = self._tittel+", "+self._artist
        return out

    #spill metoden returnerer en streng som sier at sangen blir spilt av.
    def spill(self):
         out = "Spiller "+self._tittel+" av "+self._artist+"."
         return out

    #sjekkArtist tar et navn som parameter og sjekker om navnet eller et av navnene i navn, samsvarer med artistnavnet
    def sjekkArtist(self,navn):
        status = False
        inputListe = navn.split(" ")
        artistListe = self._artist.split(" ")
        for navn in inputListe:
            if navn.lower() in artistListe:
                status = True

        return status
    
    #sjekkTittel tar en låttittel som parameter og sjekker om det stemmer med låttittelen til objektet
    def sjekkTittel(self,tittel):
        status = False
        inputListe = tittel.split(" ")
        tittelListe = self._tittel.split(" ")
        for tittel in inputListe:
            if tittel.lower() in tittelListe:
                status = True

        return status

    #sjekkArtistOgTittel kaller på sjekttTittel og sjekkArtist og returerer True om begge er True
    #og False dersom begge er False 
    def sjekkArtistOgTittel(self,artist,tittel):
        return self.sjekkTittel(tittel) and self.sjekkArtist(artist)
