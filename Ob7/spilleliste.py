from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def __str__(self):
        output = self._navn+" :"+self._sanger
        return output

    def lesFraFil(self,filnavn):
        sanger ={}
        i = 0
        fil = open(filnavn)
        for linje in fil:
            biter = linje.split(";")
            tittel = biter[0]
            artist = biter[1].strip("\n")
            sanger[i] = Sang(tittel,artist)
            self.leggTilSang(sanger[i])
            i += 1

    def leggTilSang(self,sang):
        self._sanger.append(sang)

    def fjernSang(self,sang):
        self._sanger.remove(sang)

    def finnSang(self,tittel):
        for sang in self._sanger:
            if sang.sjekkTittel(tittel):
                return sang

    def spillSang(self,sang):
        print(sang)

    def spillAlle(self):
        for sang in self._sanger:
            print(sang)

    def hentArtistUtvalg(self,artistNavn):
        nySangliste=[]
        for sang in self._sanger:
            if sang.sjekkArtist(artistNavn):
                nySangliste.append(sang)
        return nySangliste
