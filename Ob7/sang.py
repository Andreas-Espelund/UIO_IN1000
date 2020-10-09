class Sang:
    def __init__(self,artist,tittel):
        self._tittel = tittel.lower()
        self._artist = artist.lower()

    def __str__(self):
        out = self._tittel+", "+self._artist
        return out

    def spill(self):
         out = "Spiller "+self._tittel+" av "+self._artist+"."
         return out

    def sjekkArtist(self,navn):
        status = False
        inputListe = navn.split(" ")
        artistListe = self._artist.split(" ")
        for navn in inputListe:
            if navn.lower() in artistListe:
                status = True

        return status

    def sjekkTittel(self,tittel):
        status = False
        inputListe = tittel.split(" ")
        tittelListe = self._tittel.split(" ")
        for tittel in inputListe:
            if tittel.lower() in tittelListe:
                status = True

        return status


    def sjekkArtistOgTittel(self,artist,tittel):
        return self.sjekkTittel(tittel) and self.sjekkArtist(artist)
