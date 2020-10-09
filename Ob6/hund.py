class Hund:
    # Konstruktøren initialiserer Hund-objektet med oppgitt alder og vekt
    #alle hund-objektene får en instansvariabel _metthet som har verdi 10.
    def __init__(self,alder,vekt):
        self._alder = alder
        self._vekt = vekt
        self._metthet = 10

    #instansmetoden hentAlder returnerer self._alder
    def hentAlder(self):
        return self._alder

    #instansmetoden hentAlder returnerer self._vekt
    def hentVekt(self):
        return self._vekt

    #instansmetoden spring senker metthet med 1, og dersom metthet er under 5
    #går vekten ned med 1 kg.
    def spring(self):
        print("Hunden løper!")
        self._metthet -= 1
        print("Metthet gikk ned med 1")
        if self._metthet < 5:
            self._vekt -= 1
            print("Vekt gikk ned med 1 kg")

    #instansmetoden spis øker metthet med det oppgitte heltallet n,
    #dersom metthet er over 7, går vekten opp med 1kg.
    def spis(self,n):
        print(f"Hunden spiser {n} porsjoner")
        self._metthet += n
        print("Metthet gikk opp med",n)
        if self._metthet > 7:
            self._vekt += 1
            print("Vekt gikk opp med 1 kg")
