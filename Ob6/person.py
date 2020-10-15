class Person:
    #Person objektet blir initialisert med navn, alder
    #og en tom liste for hobbyer
    def __init__(self,navn,alder):
        self._navn = navn
        self._alder = alder
        self._hobbyer =[]

    #leggTilHobby legger til oppgitt hobby i listen self._hobbyer
    def leggTilHobby(self,hobby):
        self._hobbyer.append(hobby)

    #skrivHobbyer printer ut alle hobbyene på en linje
    def skrivHobbyer(self):
        s=", "
        print("Hobbyer:",s.join(self._hobbyer))

    #skrivUt printer navn og alder, så kaller jeg på skrivHobbyer
    def skrivUt(self):
        print(f"Navn: {self._navn}")
        print(f"Alder: {self._alder}")
        self.skrivHobbyer()
