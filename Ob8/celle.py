'''
Klassedefinisjon for cellene på spillebrettet

Klassen har folgende metoder:
    * settDoed
    * settLevende
    * erLevende
    * __str__

Eg valgte aa bruke en boolean verdi istedenfor at cellen sin status
var en streng "levende" eller "doed", eg syntest det er meir ryddig.
'''

class Celle:
    #cellen blir initialisert som død
    def __init__(self):
        self._lever = False

    #endrer cellen til død
    def settDoed(self):
        self._lever = False

    #endrer cellen til levende
    def settLevende(self):
        self._lever = True

    #returnerer om cellen er levende (True) eller død (False)
    def erLevende(self):
        return self._lever

    #returnerer 'O' dersom cellen er levende, eller '.' viss den er død.
    #jeg velger å bruke en __str__ metode for å gjore det lettere aa tegne brettet
    def __str__(self):
        if self._lever:
            return "O "
        else:
            return ". "
