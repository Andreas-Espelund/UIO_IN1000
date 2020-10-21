'''
Klassedefinisjon for cellene på spillebrettet
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
    def __str__(self):
        if self._lever:
            return "O"
        else:
            return "."
