'''
main for game of life spillet

Spillet lar brukeren velge spillebrett sin storrelse, antall rader og kolonner (bredde og lengde)
Brukeren kan trykke 'enter' for å oppdatere brettet helt til alle cellene er dode,
da kan brukeren trykke 'enter' igjen for aa spille paa nytt.
Brukeren kan ogsaa trykke 'q' og 'enter' for aa avslutte under eller etter spillet.
'''

#eg importerar Spillebrett klassen
from spillebrett import Spillebrett

#for aa simulere retro 'progressiv' printing til terminal
import time

#skrivGrafikk tommer skjermen og skriver en grafikk for aa gjere brukergrensesnittet finare
#den tar inn valg for kva grafikk som skal printast og kva hastigheit
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

    #her velges det riktige grafiske elementet
    if type == "start":
        grafikk = start
    if type == "end":
        grafikk = end
    if type == "skull":
        grafikk = skull

    #for-lokken skriv ut bilda
    for linje in grafikk:
        print(linje)
        time.sleep(num)

#funksjonen sjekkint kontrollerer at brukerinput er gyldig for spillebrettets dimensjonar
def sjekkint(inp):
    sjekka = False
    #eg valde å begrense spelebrettet på stoerrelse opp til 50 x 50 sidan brettet brukar lang til paa
    # aa oppdatere
    while sjekka == False:
        if inp.isdigit():
            if 0 < int(inp) <= 60:
                sjekka = True
            else:
                inp = input("Ugyldig inntasting! Skriv inn tall mellom 0 og 50!\n>")
        else:
            inp = input("Ugyldig inntasting! Skriv inn et TALL!\n>")

    return int(inp)


#main inneheld game-loopen som lar brukaren spele saa lenge den onsker
def main():
    #forst kallar eg på skrivGrafikk
    #denne metoden blir kalla flere ganger for aa ha en hovedmeny i begynnelsen av spillet
    skrivGrafikk("start",0.1)


    #brukeren velger spillebrettets stoerrelse bredde rader og lengde kolonner.
    rader = sjekkint(input("Hvor bredt skal spillebrettet vere? \n> "))
    skrivGrafikk("start",0)
    kolonner = sjekkint(input("Hvor langt skal spillebrettet vere? \n> "))

    #det blir saa laget et Spillebrett, nyttBrett
    nyttBrett = Spillebrett(rader,kolonner)
    skrivGrafikk("start",0)

    #valg gjoer at programmet venter paa brukeren foer det fortsetter, og gir brukeren muligheten til aa avslutte
    kjorer = True
    valg = input("Trykk 'enter' for aa fortsette, skriv inn 'q' og trykk enter for aa avslutte: \n>").lower()
    if valg == "q":
        kjorer = False

    #spelet gaar saa lenge valg ikkje er 'q'
    while kjorer:
        #brettet blir tegnet
        nyttBrett.tegnBrett()

        print("")
        #prosentbar-en som viser andel levende blir oppdatert
        nyttBrett.lagProsentBar()
        print("")

        #statestikken om spillbrettet blir printa
        print(nyttBrett.lagStatestikk())

        #dersom alle cellene er dode, er rund ferdig og brukeren kan avslutte eller spele igjen
        if nyttBrett.finnAntallLevende() == 0:
            skrivGrafikk("skull",0.05)
            print("** Alle cellene er døde! **")
            kjorer = False
            #brukeren har ogsaa muligheten til a vise sin respekt for de avdoede cellene
            respekt = input("Press 'F' to pay respects. \n>").lower()


        #dersom det forsatt er levende celler, kan brukeren oppdatere brettet eller avslutte
        else:
            valg = input("Trykk 'enter' for aa fortsette, skriv inn 'q' og trykk enter for aa avslutte: \n>").lower()
            if valg == "q":

                kjorer = False

        nyttBrett.oppdatering()

    #brukaren kjem tilbake til hovedmeny/startskjemen og faar valget om aa starte et nytt spel eller avslutte
    skrivGrafikk("start",0.1)
    valg = input("Trykk 'enter' for aa spille på nytt, skriv inn 'q' og trykk enter for aa avslutte: \n>").lower()
    #dersom brukaren skriv 'q' printar avsultningskjermen og programmet avsluttast, ellers blir main kalla paa nytt
    if valg == "q":
        skrivGrafikk("end",0.1)

        #liten bonus med try except
        try:
            respekt == "f"
        except:
            pass
        else:
            if respekt == "f":
                print("Thanks for the respects")

    else:
        main()

#kall paa main
main()
