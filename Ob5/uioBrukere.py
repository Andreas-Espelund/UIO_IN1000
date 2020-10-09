'''
Dette programmet lar brukeren skrive inn sitt navn og en epost suffix.
Via en enkel terminal bruker-interface som lar brukreren lage et brukernavn og
en epostadresse.
'''

#studentenes informasjon lagres i ordboken studenter
studenter={}

#lagBrukernavn tar inn navn, og returnerer et brukernavn
def lagBrukernavn(navn,ordbok):
    biter = navn.split(" ")
    fornavn = biter[0].lower()
    etternavn = biter[-1].lower()
    brukernavn =fornavn+etternavn[0]

    i = 1
    while brukernavn in ordbok:
        brukernavn += etternavn[i]
        i +=1
    return brukernavn

#lag epost tar brukernavnet og epost suffix-et inn og returnerer epostadressen
def lagEpost(brukernavn,suffix):
    return brukernavn+'@'+suffix

#inputSjekk kontrollerer input og sjekker at der er minimum 1 mellomrom, og
#minst 2 bokstaver, slik sjekker vi at det er et fornavn, mellomrom, etternavn.
def inputSjekk(inp):
    verifisert = False
    while verifisert == False:
        bokstav = 0
        mellomrom = 0
        for char in inp:
            if char.isalpha():
                bokstav +=1
            elif char == " ":
                mellomrom +=1

        if (len(inp) == (bokstav + mellomrom)) and (mellomrom >0) and (bokstav >=2):
            verifisert = True
        else:
            inp = input("Skriv inn navn OG etternavn (husk mellomrom): ")
    return inp

#printEposter tar inn ordboken og returnerer alle brukerene sine eposter
def printEposter(ordbok):
    for brukernavn in ordbok:
        print(lagEpost(brukernavn,ordbok[brukernavn]))

#test_lagBrukernavn tester funksjonen lag lagBrukernavn
def test_lagBrukernavn():
    #standard case
    resultatBrukernavn = lagBrukernavn("Andreas Espelund",studenter)
    korrektBrukernavn = "andrease"
    assert resultatBrukernavn == korrektBrukernavn, "Forventet " +\
    korrektBrukernavn + " men fikk " + resultatBrukernavn

    #dersom brukeren legger inn mellomnavn
    resultatBrukernavn = lagBrukernavn("Andreas Raftevold Espelund",studenter)
    korrektBrukernavn = "andrease"
    assert resultatBrukernavn == korrektBrukernavn, "Forventet " +\
    korrektBrukernavn + " men fikk " + resultatBrukernavn

    #dersom brukeren skriver inn store bokstaver
    resultatBrukernavn = lagBrukernavn("ANDREAS ESPELUND",studenter)
    korrektBrukernavn = "andrease"
    assert resultatBrukernavn == korrektBrukernavn, "Forventetft " +\
    korrektBrukernavn + " men fikk " + resultatBrukernavn

    #dersom brukernavnet allerede er tatt
    resultatBrukernavn = lagBrukernavn("Andreas Espelund",{"andrease":"testordbok"})
    korrektBrukernavn = "andreases" #vi forventer å få lagt til en bokstav til fra etternavnet 's'
    assert resultatBrukernavn == korrektBrukernavn, "Forventet " +\
    korrektBrukernavn + " men fikk " + resultatBrukernavn

#test_lagEpost tester funksjonen lagEpost
def test_lagEpost():
    resultatEpost = lagEpost("andrease","ifi.uio.no")
    korrektEpost = "andrease@ifi.uio.no"
    assert resultatEpost == korrektEpost, "Forventet " +\
    korrektEpost + " men fikk " + resultatEpost

    resultatEpost = lagEpost("","ifi.uio.no")
    korrektEpost = "@ifi.uio.no"
    assert resultatEpost == korrektEpost, "Forventet " +\
    korrektEpost + " men fikk " + resultatEpost

    resultatEpost = lagEpost("","")
    korrektEpost = "@"
    assert resultatEpost == korrektEpost, "Forventet " +\
    korrektEpost + " men fikk " + resultatEpost

#hovedprogram inneholder alle funksjonskallene og while løkken som lar brukeren
#velge funksjon.
def hovedprogram():
    test_lagBrukernavn()
    test_lagEpost()

    run = True
    while run == True:
        valg = input("Velg funksjon (i/p/s): ").lower()

        #dersom brukren skriver inn "i", skriver bruker inn navn og suffix og
        #det blir laget et brukernavn som blir lagt til i studenter med suffixet.
        if valg == "i":
            navn = inputSjekk(input("Skriv inn navn: "))
            suffix = input("Skriv inn mail suffix: ")
            brukernavn = lagBrukernavn(navn,studenter)
            studenter[brukernavn]=suffix

        #skriver brukeren inn 'p' kalles det på printEposter
        elif valg == "p":
            printEposter(studenter)

        #skriver brukeren inn 's' blir run False,while løkken brytes og programmet stopper
        elif valg == "s":
            run = False

        #dersom brukeren skriver inn noe ugyldig, printes denne feilmeldingen.
        else:
            print("Prøv igjen..")

#kall på hovedprogram
hovedprogram()
