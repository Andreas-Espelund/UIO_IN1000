'''
Hovedprogram for game of life spillet

Spillet lar brukeren velge spillebrett sin storrelse, antall rader og kolonner (bredde og lengde)
Brukeren kan trykke 'enter' for å oppdatere brettet helt til alle cellene er dode,
da kan brukeren trykke 'enter' igjen for aa spille paa nytt.
Brukeren kan ogsaa trykke 'q' og 'enter' for aa avslutte under eller etter spillet.

'''

#jeg importerer Spillebrett klassen
from spillebrett import Spillebrett

import time

#skrivGrafikk tommer skjermen og skriver en grafikk for aa gjore brukergrensesnittet penere
def skrivGrafikk(type,num):
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

    skull =[
    "         _,.-------.,_",
    "     ,;~'             '~;,",
    "   ,;                     ;,",
    "  ;                         ;",
    " ,'                         ',",
    ",;                           ;,",
    "; ;      .           .      ; ;",
    "| ;   ______       ______   ; |",
    "|  `/~''     ~'' . ''~  '~ '  |",
    "|  ~  ,-~~~^~, | ,~^~~~-,  ~  |",
    " |   |        }:{        |   |",
    " |   l       / | \       !   |",
    " .~  (__,.--' .^. '--.,__)  ~.",
    " |     ---;' / | \ `;---     |",
    "  \__.       \/^\/       .__/",
    "   V| \                 / |V",
    "    | |T~\___!___!___/~T| |",
    "    | |`IIII_I_I_I_IIII'| |",
    "    |  \,III I I I III,/  |",
    "     \   `~~~~~~~~~~'    /",
    "       \   .       .   /",
    "         \.    ^    ./",
    "           ^~~~^~~~^"
    ]


    if type == "start":
        grafikk = start
    if type == "end":
        grafikk = end
    if type == "skull":
        grafikk = skull

    for linje in grafikk:
        print(linje)
        time.sleep(num)

#funksjonen sjekkint kontrollerer at brukerinput er gyldig for spillebrettets dimensjoner
def sjekkint(inp):
    sjekka = False

    while sjekka == False:
        if inp.isdigit():
            if 0 < int(inp) <= 60:
                sjekka = True
            else:
                inp = input("Ugyldig inntasting! Skriv inn tall mellom 0 og 50!")
        else:
            inp = input("Ugyldig inntasting! Skriv inn et TALL!")

    return int(inp)

#hovedprogram inneholder game-loopen som lar brukeren spille saa lenge den onsker
def hovedprogram():
    #forst kaller jeg på skrivGrafikk
    #denne metoden blir kalt flere ganger for aa ha en hovedmeny i begynnelsen av spillet
    skrivGrafikk("start",0.1)


    #brukeren velger spillebrettets stoerrelse bredde x og lengde y.
    x = sjekkint(input("Hvor bredt skal spillebrettet vere? \n> "))
    skrivGrafikk("start",0)
    y = sjekkint(input("Hvor langt skal spillebrettet vere? \n> "))

    #det blir saa laget et Spillebrett, nyttBrett
    nyttBrett = Spillebrett(x,y)
    skrivGrafikk("start",0)
    #valg gjoer at programmet venter paa brukeren foer det fortsetter, og gir brukeren muligheten til aa avslutte

    kjorer = True
    valg = input("Trykk 'enter' for aa fortsette, skriv inn 'q' og trykk enter for aa avslutte: \n>").lower()
    if valg == "q":
        kjorer = False

    #spillet gaar saa lenge valg ikke er 'q'
    while kjorer:
        #brettet blir tegnet
        nyttBrett.tegnBrett()
        #statestikken om spillbrettet blir printet
        print("")
        nyttBrett.lagProsentBar()
        print("")
        print(nyttBrett.lagStatestikk())
        #dersom alle cellene er dode, er runden ferdig og brukeren kan avslutte eller spille igjen

        if nyttBrett.finnAntallLevende() == 0:
            skrivGrafikk("skull",0.05)
            print("** Alle cellene er døde! **")
            kjorer = False
            respekt = input("Press 'F' to pay respects. \n>").lower()


        #dersom det forsatt er levende celler, kan brukeren oppdatere brettet eller avslutte
        else:
            valg = input("Trykk 'enter' for aa fortsette, skriv inn 'q' og trykk enter for aa avslutte: \n>").lower()
            if valg == "q":

                kjorer = False

        nyttBrett.oppdatering()

    #dersom brukeren har avsluttet spillet printes 'farvel-skjermen'
    skrivGrafikk("start",0.1)
    valg = input("Trykk 'enter' for aa spille på nytt, skriv inn 'q' og trykk enter for aa avslutte: \n>")
    if valg == "q":
        skrivGrafikk("end",0.1)
        try:
            respekt == "f"
        except:
            pass
        else:
            if respekt == "f":
                print("Thanks for the respects")

    else:
        hovedprogram()

#kall paa hovedprogram
hovedprogram()
