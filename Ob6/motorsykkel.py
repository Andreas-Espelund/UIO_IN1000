class Motorsykkel:
    
    #konstruktøren lager et motorsykkel-objekt med instansvariablene
    #_merke,_regnr og _kmStand.
    def __init__(self,merke,regnr,km):
        self._merke = merke
        self._regnr = regnr
        self._kmStand = km

    #kjor oker _kmStand med km som er parameteret for metoden
    def kjor(self,km):
        self._kmStand += km

    #instansmetoden hentKilometerstand returnerer Kilometerstanden til objektet
    def hentKilometerstand(self):
        return self._kmStand

    #skrivUt printer en streng med merke,regnr og Kilometerstanden til sykkelen
    def skrivUt(self):
        print(f"Motorsykkelen er en {self._merke} med registreringsnummer" \
        f"{self._regnr} som har kjørt {self._kmStand} km.")
