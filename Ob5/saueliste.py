'''
Oppg.5                       **OPPGAVETEKST**
Foreldrene til andreas har en gaard med sauer som skal veies flere ganger hver host.
For å gjore dette lettere har de en elektronisk oremerkescanner som leser av oremerker
med RFID chip på fra sauene når de veies. De skriver også inn vekten på scanner-enheten.
Når de henter ut data fra denne scanneren kommer det som den vedlagte .csv filen.

Lag et program som kan gjore det enklere for de å lese den informasjonen
(oremerkenummer og vekt).

1.Lag en ordbok nummerOgVekt som inneholder oremerkenummeret og vekten ved å
  hente inn data fra filen "avleserdata.csv"
  tips: lagre oremerke som oremerkenummeret-268981000000. Fordi alle de forste sifferene
  i nummeret er like så dette gjor det enklere å lese oremerkenummeret.

2.Lag en funksjon som skriver ut innholdet i ordboken på en måte som er enkel
  å lese. (Gjerne med sortering)

3.Legg til en funksjon som gjor at de kan finne en vekt ved å soke på nummer.

4.Lag et brukergrensesnitt med en while loop som gjor at de kan velge hva de
  vil gjore ved å taste inn eks. 1 for å printe ordboken, 2 for å soke på nummer osv.

5.Valgfritt! Lag en funksjon som lager en .txt fil med nummer og vekter.

'''


#filavlesning leser inn en vil fra RFID scanneren og returnerer en ordbok med
#øremerkenummer og vekt.
def filavlesning():
    #jeg åpner filen og kaller den avleserdata
    #jeg måtte legge til type encoding på fila fordi den fikk med uønska spesialtegn
    avleserdata = open("avleserdata.csv",encoding='utf-8-sig')

    #ordboken nummerOgVekt blir definert
    nummerOgVekt ={}

    #for lokken itererer gjennom avleserdata og henter kun ut merkenummer og vekt
    #deretter legger den disse til i ordboken
    for linje in avleserdata:
        deltElement = linje.split(";")
        oremerke = int(deltElement[0])-268981000000
        nummerOgVekt[oremerke]=int(deltElement[2])
    return nummerOgVekt


#her sorterer jeg listen etter nummer og vekt, både stigende og synkende
def ordboksortering(ordbok):

    #jeg lagar to nye ordbøker som er sortert etter nøklene, stigende og synkende
    stigendeNummer = dict(sorted(ordbok.items()))

    synkendeNummer = dict(sorted(ordbok.items(),reverse=True))

    #jeg gjør det samme for de to neste, bare at her setter jeg vekt som
    #nøkkelen det skal sorteres etter ved hjelp av lambda nøkkelordet.

    stigendeVekt = dict(sorted(ordbok.items(),key=lambda vekt:vekt[1]))

    synkendeVekt =dict(sorted(ordbok.items(),key=lambda vekt:vekt[1],reverse=True))

    #jeg lager en ordbok som inneholder alle de sorterte ordbøkene
    sorterteOrdboker ={
    "stigendeNummer":stigendeNummer,
    "synkendeNummer":synkendeNummer,
    "stigendeVekt":stigendeVekt,
    "synkendeVekt":synkendeVekt
    }

    return sorterteOrdboker

#funksjonen skriv ut skriver ut nummer og vekt på en oversiktlig måte
def skrivUt(ordbok):
    for individ in ordbok:
        print(f'Oremerke: {individ:03d}    Vekt: {ordbok[individ]} kg')


#sjekkInt sjekker brukerinputen på menyvalget
def sjekkInt(num):
    while num.isdigit() == False:
        num = input("Skriv inn gyldig nummer! : ")
    return int(num)


#hent vekt lar brukeren soke etter en vekt med oremerkenummer
def hentVekt(ordbok):
    num = sjekkInt(input("Skriv inn oremerkenummer: "))
    for individ in ordbok:
        if num == individ:
            print(f'Oremerke: {individ:03d}    Vekt: {ordbok[individ]} kg')
    if num not in ordbok.keys():
        print("Det oppgitte nummeret er ikke på lista.")


#tomskjerm printer tomme linjer og en grafikk for å gjore programmet mer ryddig
#parameteret gjer slik at en kan tømme skjermen, eller tømme skjermen og printe
#grafikken
def tomskjerm(txt):
    grafikk = [
    '░██████╗░█████╗░██╗░░░██╗███████╗██╗░░░██╗███████╗██╗░░██╗████████╗',
    '██╔════╝██╔══██╗██║░░░██║██╔════╝██║░░░██║██╔════╝██║░██╔╝╚══██╔══╝',
    '╚█████╗░███████║██║░░░██║█████╗░░╚██╗░██╔╝█████╗░░█████═╝░░░░██║░░░',
    '░╚═══██╗██╔══██║██║░░░██║██╔══╝░░░╚████╔╝░██╔══╝░░██╔═██╗░░░░██║░░░',
    '██████╔╝██║░░██║╚██████╔╝███████╗░░╚██╔╝░░███████╗██║░╚██╗░░░██║░░░',
    '╚═════╝░╚═╝░░╚═╝░╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░'
    ]

    for i in range(100):
        print("")
    if txt == 0:
        for line in grafikk:
            print(line)


#eksporterFil lar brukeren velge filnavn og lager en ny tekstfil med
#oremerkenummer og vekt
def eksporterFil(ordbok):
    filnavn = input("Velg filnavn: ")
    out = open(f"{filnavn}.txt","w")
    for individ in ordbok:
        out.write(f'Oremerke: {individ:03d}    Vekt: {ordbok[individ]} kg\n')
    out.close()


#orbokValg lar brukeren velge hvilken sortert liste som skal brukes
def orbokValg(ordbok):
    print("1.Stigende vekt")
    print("2.Synkende vekt")
    print("3.Stigende Oremerke")
    print("4.Synkende Oremerke")

    valg = sjekkInt(input("Skriv inn nummer! (1/2/3/4):"))
    while valg not in range(1,5):
        valg = sjekkInt(input("Skriv inn nummer! (1/2/3/4):"))

    if valg == 1:
        return ordbok['stigendeVekt']
    elif valg == 2:
        return ordbok['synkendeVekt']
    elif valg == 3:
        return ordbok['stigendeNummer']
    elif valg == 4:
        return ordbok['synkendeNummer']

    else:
        print("Ugyldig input!")


#while lokken lar brukeren velge funksjon og den går så lenge go = True
def hovedprogram():
    filOrdbok = filavlesning()
    sortert = ordboksortering(filOrdbok)

    go = True
    while go == True:
        tomskjerm(0)
        print("1. Vis liste")
        print("2. Finn vekt med oremerkenummer")
        print("3. Skriv ut liste som .txt")
        print("4. Avslutt")
        valg = sjekkInt(input("Skriv inn et nummer! (1/2/3/4): "))

        #dersom brukeren skriver 1 kalles det på skrivUt
        if valg == 1:
            tomskjerm(1)
            liste = orbokValg(sortert)
            skrivUt(liste)
            x = input("Trykk en tast for å gå tilbake")

        #dersom brukeren skriver 2 kalles det på hentVekt
        elif valg == 2:
            tomskjerm(1)
            hentVekt(filOrdbok)
            x = input("Trykk en tast for å gå tilbake")

        #dersom brukeren skriver inn 3 kalles det på eksporterFil
        elif valg == 3:
            tomskjerm(1)
            liste = orbokValg(sortert)
            eksporterFil(liste)
            print("Vellykket!")
            x = input("Trykk en tast for å gå tilbake")

        #dersom brukeren skriver inn 4, blir go = False og programmet avsluttes
        elif valg == 4:
            go = False

        #viss brukeren tastet noe annet må brukeren taste inn på nytt.
        else:
            x =input("Ugyldig inntasting, trykk for å prove på nytt!")


hovedprogram()
