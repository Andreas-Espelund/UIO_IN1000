'''
Klassedefinisjon for Sang:

Klassen har instansvariablene _tittel og _artist, og 
metodene spill, sjekkArtist, sjekkTittel og sjekkArtistOgTittel. 
'''
import simpleaudio as sa

class Sang:
    #Sang-objekta blir initialisert med _artist og _tittel som instansvariablar
    def __init__(self,artist,tittel,filnavn):
        self._tittel = tittel.lower()
        self._artist = artist.lower()
        self._filnavn = filnavn
    #__str__ returnerer artistnavn og låtnavn på ein lesbar måte
    def __str__(self):
        out = self._tittel+", "+self._artist
        return out

    #spill metoden returnerer ein streng som seier at sangen blir spelt av.
    def spill(self):
         out = "Spiller "+self._tittel+" av "+self._artist+"."
         print(out)
         wave_obj = sa.WaveObject.from_wave_file(self._filnavn)
         play_obj = wave_obj.play() 
         play_obj.wait_done()


    #sjekkArtist tar eit navn som parameter og sjekker om navn eller et av navnene i navn, samsvarer med artistnavnet
    def sjekkArtist(self,navn):
        status = False
        inputListe = navn.split(" ")
        artistListe = self._artist.lower().split(" ")
        for navn in inputListe:
            if navn.lower() in artistListe:
                status = True
               
        return status
    
    #sjekkTittel tar ein låttittel som parameter og sjekkar om det stemmar med låttittelen til objektet
    def sjekkTittel(self,tittel):
        status = False
        inputListe = tittel.split(" ")
        tittelListe = self._tittel.lower().split(" ")
        for tittel in inputListe:
            if tittel.lower() in tittelListe:
                status = True

        return status

    #sjekkArtistOgTittel kallar på sjekttTittel og sjekkArtist og returerar True om begge er True
    #og False dersom begge er False 
    def sjekkArtistOgTittel(self,artist,tittel):
        return self.sjekkTittel(tittel) and self.sjekkArtist(artist)
