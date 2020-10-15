'''
Dette programmet tester klassen Dato
'''
from dato import Dato

#brukerinput sjekker om brukeren har oppgitt en gyldig dato, den tar ikke høyde for
#skuddaar. Den sjekker også at det er oppgitt i formatet DDMMYYYY
def brukerinput(inp):
    sjekka = False
    #dagerIMnd inneholder en nokkel for hver måned med en innholdsverdi
    #for antall dager i måneden
    dagerIMnd={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    while sjekka == False:
        dag = inp[0:2]
        maaned = inp[2:4]
        aar = inp[4:8]

        if len(inp) == 8:
            if (0 < int(maaned) <= 12) and (0 <= int(aar)):
                if 0 < int(dag) <= dagerIMnd[int(maaned)]:
                    sjekka = True
                else:
                    inp = input("Ugyldig dag! Prøv igjen (DDMMYYYY): ")

            else:
                inp = input("Ugyldig maaned eller aar! Prøv igjen (DDMMYYYY): ")
        else:
            inp = input("Ugyldig format! Prøv igjen (DDMMYYYY): ")

    dato = dag + "." + maaned + "." + aar
    return dato


#testfunksjon for brukerinput
def testBrukerinput():
    rersultatDato = brukerinput("17012000")
    korrektDato = "17.01.2000"

    assert rersultatDato == korrektDato, ("forventa ",korrektDato," men fikk ",rersultatDato)


#spesiellDag sjekker om det er lønningsdag eller en helt ny måned
def spesiellDag(dato):
    if dato.erDag(15):
        print("Lonningsdag!")
    elif dato.erDag(1):
        print("Ny maaned, ny muligheteter!")


#hovedprogram inneholder alle opprettelsen av objekt, kall på instansmetoder,funksjoner osv.
def hovedprogram():

    #jeg tester brukerinput
    testBrukerinput()

    #jeg lager objektet dato1
    dato1 = Dato(15,12,2020)

    #datoens aar blir skrevet ut ved å kalle på .lesAar
    print("Aar: ",dato1.lesAar())

    #jeg kaller på spesiellDag
    spesiellDag(dato1)

    #jeg skriver ut datoen som en enkelt lesbar streng
    lesbarDato = dato1.lagStreng()
    print("Dato:",lesbarDato)

    #jeg endrer dato til neste dag med .nesteDag, og printer datoen på nytt
    dato1.nesteDag()
    lesbarDato = dato1.lagStreng()
    print("Dato:",lesbarDato)

    #brukerens dato input blir kontrollert og lagra i inputDato
    inputDato = brukerinput(input("Skriv inn dato (DDMMYYYY): "))
    print(inputDato,dato1.rekkefolge(inputDato),lesbarDato)


hovedprogram()
