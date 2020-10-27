'''
Hovedprogram for game of life spillet

Spillet lar brukeren velge spillebrett sin storrelse, antall rader og kolonner (bredde og lengde)
Brukeren kan trykke 'enter' for å oppdatere brettet helt til alle cellene er dode,
da kan brukeren trykke 'enter' igjen for aa spille paa nytt.
Brukeren kan ogsaa trykke 'q' og 'enter' for aa avslutte under eller etter spillet.

'''

#jeg importerer Spillebrett klassen
from spillebrett import Spillebrett

#skrivGrafikk tommer skjermen og skriver en grafikk for aa gjore brukergrensesnittet penere
def skrivGrafikk(type):
    for i in range(100):
        print("")

    start = [
    "░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░███████╗  ██╗░░░░░██╗███████╗███████╗",
    "██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██╔════╝  ██║░░░░░██║██╔════╝██╔════╝",
    "██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║█████╗░░  ██║░░░░░██║█████╗░░█████╗░░",
    "██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║██╔══╝░░  ██║░░░░░██║██╔══╝░░██╔══╝░░",
    "╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝██║░░░░░  ███████╗██║██║░░░░░███████╗",
    "░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░╚═╝░░░░░  ╚══════╝╚═╝╚═╝░░░░░╚══════╝"
     ]
    end = [
    "██╗░░██╗░█████╗░  ██████╗░███████╗████████╗  ██████╗░██████╗░░█████╗░██╗",
    "██║░░██║██╔══██╗  ██╔══██╗██╔════╝╚══██╔══╝  ██╔══██╗██╔══██╗██╔══██╗██║",
    "███████║███████║  ██║░░██║█████╗░░░░░██║░░░  ██████╦╝██████╔╝███████║██║",
    "██╔══██║██╔══██║  ██║░░██║██╔══╝░░░░░██║░░░  ██╔══██╗██╔══██╗██╔══██║╚═╝",
    "██║░░██║██║░░██║  ██████╔╝███████╗░░░██║░░░  ██████╦╝██║░░██║██║░░██║██╗",
    "╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░╚══════╝░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝"
    ]

    if type == "start":
        grafikk = start
    elif type == "end":
        grafikk = end

    for linje in grafikk:
        print(linje)

#funksjonen sjekkint kontrollerer at brukerinput er gyldig for spillebrettets dimensjoner
def sjekkint(inp):
    sjekka = False

    while sjekka == False:
        if inp.isdigit():
            if 0 < int(inp) <= 60:
                sjekka = True
            else:
                inp = input("Ugyldig inntasting! Skriv inn tall mellom 0 og 60!")
        else:
            inp = input("Ugyldig inntasting! Skriv inn et TALL!")

    return int(inp)

#hovedprogram inneholder game-loopen som lar brukeren spille saa lenge den onsker
def hovedprogram():
    #forst kaller jeg på skrivGrafikk
    #denne metoden blir kalt flere ganger for aa ha en hovedmeny i begynnelsen av spillet
    skrivGrafikk("start")


    #brukeren velger spillebrettets stoerrelse bredde x og lengde y.
    x = sjekkint(input("Hvor bredt skal spillebrettet vere? \n> "))
    skrivGrafikk("start")
    y = sjekkint(input("Hvor langt skal spillebrettet vere? \n> "))

    #det blir saa laget et Spillebrett, nyttBrett
    nyttBrett = Spillebrett(x,y)
    skrivGrafikk("start")
    #valg gjoer at programmet venter paa brukeren foer det fortsetter, og gir brukeren muligheten til aa avslutte
    valg = input("Press 'enter' for aa fortsette, skriv inn 'q' og trykk enter for aa avslutte: \n>")

    #spillet gaar saa lenge valg ikke er 'q'
    while valg != "q":
        #brettet blir tegnet
        nyttBrett.tegnBrett()
        #statestikken om spillbrettet blir printet
        print(nyttBrett.lagStatestikk())
        #dersom alle cellene er dode, er runden ferdig og brukeren kan avslutte eller spille igjen
        if nyttBrett.finnAntallLevende() == 0:
            print("** Alle cellene er døde! **")
            start = input("Trykk 'enter' for aa spille igjen, trykk 'q' og enter for aa avslutte: \n>")
            if start == "q":
                valg = "q"
            else:
                hovedprogram()

        #dersom det forsatt er levende celler, kan brukeren oppdatere brettet eller avslutte
        else:
            valg = input("Press 'enter' for aa fortsette, skriv inn 'q' og trykk enter for aa avslutte: \n>")
            nyttBrett.oppdatering()

    #dersom brukeren har avsluttet spillet printes 'farvel-skjermen'
    skrivGrafikk("end")

#kall paa hovedprogram
hovedprogram()
