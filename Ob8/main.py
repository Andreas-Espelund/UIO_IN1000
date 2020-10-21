'''
Hovedprogram for game of life spillet
'''

from spillebrett import Spillebrett
from celle import Celle


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


def sjekkint(inp):
    sjekka = False

    while sjekka == False:
        if inp.isdigit():
            if 0 < int(inp) < 50:
                sjekka = True
            else:
                inp = input("Ugyldig inntasting! Skriv inn tall mellom 0 og 50!")
        else:
            inp = input("Ugyldig inntasting! Skriv inn et TALL!")

    return int(inp)

def hovedprogram():

    skrivGrafikk("start")


    #velg spillebrettstorrelse
    x = sjekkint(input("Hvor bredt skal spillebrettet vere? \n> "))
    skrivGrafikk("start")
    y = sjekkint(input("Hvor langt skal spillebrettet vere? \n> "))
    nyttBrett = Spillebrett(x,y)
    skrivGrafikk("start")
    valg = input("Press 'enter' for aa fortsette, skriv inn 'q' og trykk enter for aa avslutte: \n>")

    while valg != "q":
        nyttBrett.tegnBrett()
        print(nyttBrett.lagStatestikk())
        valg = input("Press 'enter' for aa fortsette, skriv inn 'q' og trykk enter for aa avslutte: \n>")
        nyttBrett.oppdatering()

    skrivGrafikk("end")

hovedprogram()
