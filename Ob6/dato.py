class Dato:

    #konstruktøren lager et dato objekt med instansvariablene _dag, _maaned og _aar
    def __init__(self,nyDag,nyMaaned,nyttAar):
        self._dag = int(nyDag)
        self._maaned = int(nyMaaned)
        self._aar = int(nyttAar)


    #lesAar returnerer instansvariablen for aar
    def lesAar(self):
        return self._aar


    #lagStreng returnerer datoen som streng i formatet dd.mm.yyyy
    def lagStreng(self):
        return str(self._dag)+"."+str(self._maaned)+"."+str(self._aar)


    #erDag tar en dag som parameter og returnerer true dersom den er lik self._dag, false viss ikke
    def erDag(self,dag):
        return self._dag == int(dag)


    #rekkefolge tar en dato som parameter og sammenligner den med objektet
    def rekkefolge(self,inpDato):
        dato = inpDato.split(".")

        #jeg splitter inputdatoen i dag, maaned og aar og lagrer de som heltall
        inpDag = int(dato[0])
        inpMaaned = int(dato[1])
        inpAar = int(dato[2])

        #jeg sammenligner aar, eller aar og maned, eller aar og maaned og dag.
        if (inpAar > self._aar) or ((inpMaaned >self._maaned) and (inpAar >= self._aar)) or \
            ((inpDag > self._dag) and (inpMaaned >= self._maaned) and (inpAar >= self._aar)):
            rekkefolge = "kommer etter"

        elif (inpAar < self._aar) or ((inpMaaned < self._maaned) and (inpAar <= self._aar)) or \
            ((inpDag < self._dag) and (inpMaaned <= self._maaned) and (inpAar <= self._aar)):
            rekkefolge = "kommer foer"

        else:
            rekkefolge = "er samme dato som"

        #strengen rekkefolge rekkefølgen til inp dato i forhold til objektet
        return rekkefolge


    #nesteDag endrer dato til neste dag, den tar ikke hoyde  for skuddaar
    def nesteDag(self):
        #dagerIMnd inneholder en nokkel for hver måned med en innholdsverdi
        #for antall dager i måneden
        dagerIMnd={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

        #if testen sjekker først om dagen er den siste i maaneden
        if self._dag < dagerIMnd[self._maaned]:
            self._dag +=1
        #om den er det sjekker den om maaneden er den siste i aaret
        elif self._maaned < 12:
            self._maaned += 1
            self._dag = 1
        #dersom både dagen er siste i maaneden og maaneden er siste i aaret,
        #går vi  til 1.jan i det nest aaret
        else:
            self._aar += 1
            self._maaned = 1
            self._dag = 1


        print("Dato er endret til neste dag!")
