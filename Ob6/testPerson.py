'''
Dette programmet tester klassen Person. Jeg gjør dette ved å la brukeren skrive inn navn,
alder og hobbyer.
'''
#først importeres klassen Person fra filen person.py
from person import Person

#strSjekk lar kun brukeren oppgi bokstaver(til navn og hobbyer)
def strSjekk(inp):
    while not inp.isalpha():
        inp = strSjekk(input("Kun bokstaver: "))
    return inp

#strSjekk sjekker at brukeren oppgir tall (til alder)
def intSjekk(inp):
    while not inp.isdigit():
        inp = input("Kun POSITIVE HELTALL:")
    return inp

#hovedprogram kaller alle funksjonene og instansmetodene
def hovedprogram():
    #brukeren oppgir gyldig navn og alder
    navn = strSjekk(input("Skriv inn navn: ")).capitalize()
    alder = intSjekk(input("Skriv inn alder: ")).capitalize()
    #jeg lager pers som er et objekt i klassen Person med navn og alder
    pers = Person(navn,alder)

    #While løkken lar brukeren legge til hobbyer helt til den taster inn "s"
    inp = strSjekk(input("Legg til hobby (Tast inn 's' for å avslutte): "))
    while inp != "s":
        pers.leggTilHobby(inp.capitalize())
        inp = strSjekk(input("Legg til hobby (Tast inn 's' for å avslutte): "))

    #til slutt skrives det ut statestikken om pers
    pers.skrivUt()

#kall på hovedprogram
hovedprogram()
