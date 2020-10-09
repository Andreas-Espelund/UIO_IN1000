'''
Oppgave 6:
Lag et program som lar brukeren legge til venners navn med bursdag, printe ut en
bursdag ved hjelp av navn eller printe ut en oversikt over alle vennene sine
bursdager. Lagre vennen sine navn som nøkkelen i en ordbok og datoene som verdiene.

Lag en brukerinterface som lar brukeren velge ulike funksjoner lett og la
programmet kjøre helt til brukeren avslutter det. Bygg inn en funksjon for å
la brukeren avslutte programmet.
'''

vennersBursdag = {}
# leggTil tar inn navn og dato fra brukeren og legger det til ordboken
def leggTil():
    navn = strSjekk(input("Skriv inn navn: \n>"))
    dato = datoSjekk(input("Skriv inn dato: (DDMM): \n>"))
    if navn in vennersBursdag:
        print(f"Dette navnet er allerede registrert! Du kan legge til første bokstav i etternavnet for å skille mellom de.")
        hold = input("Trykk en tast for å gå tilbake")
    else:
        vennersBursdag[navn.lower()] = dato
        hold = input("Trykk en tast for å gå tilbake")

#Sjekker at oppgitt parameter er bokstaver
def strSjekk(navn):
    sjekka = False
    while sjekka == False:
        if navn.isalpha():
            output = navn
            sjekka = True
        else:
            navn = input("Skriv inn navn (KUN bokstaver): \n>")
    return output.lower()

# datoSjekk kontrollerer at den oppgitte datoen er tall, i rett format og at
# datoen er gyldig.
def datoSjekk(dato):
    sjekka = False
    while sjekka == False:
        if dato.isdigit() and len(dato) == 4:
            dag = dato[0:2]
            mnd = dato[2:4]
            if int(dag) in range(0,32) and int(mnd) in range(0,13):
                dato = dag+'.'+mnd
                sjekka = True
            else:
                dato = input("Ugyldig dato! Skriv inn dato (DDMM): \n>")
        else:
            dato = input("Skriv inn dato (DDMM) Kun tall, fire siffer: \n>")
    return dato

# finn bursdag tar en navn som parameter og finner verdien til navnet i
# ordboken og printer navn og dato.
def finnBursdag(navn):
    if navn in vennersBursdag:
        print(f'Bursdagen til {navn} er {vennersBursdag[navn]}.')
        hold = input("Trykk en tast for å gå tilbake")
    else:
        print(f'{navn} er ikke registrert!')
        hold = input("Trykk en tast for å gå tilbake")

# printAlle printer alle de registrerte navnene med bursdager
def printAlle():
    print("Dine venners bursdager:")
    for navn in vennersBursdag:
        print(f'Bursdagen til {navn} er {vennersBursdag[navn]}.')
    hold = input("Trykk en tast for å gå tilbake")

# tomSkjerm printer 100 tomme linjer for å tømme skjermen slik at
# brukergrensesnittet ser penere ut
def tomSkjerm():
    i = 0
    for i in range(100):
        print("")
        i += 1

# velkommen printar ut en grafikk slik at programmet ser litt kulare ut. :)
def velkommen():
    bursdager = [
    "██████╗░██╗░░░██╗██████╗░░██████╗██████╗░░█████╗░░██████╗░███████╗██████╗░",
    "██╔══██╗██║░░░██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝░██╔════╝██╔══██╗",
    "██████╦╝██║░░░██║██████╔╝╚█████╗░██║░░██║███████║██║░░██╗░█████╗░░██████╔╝",
    "██╔══██╗██║░░░██║██╔══██╗░╚═══██╗██║░░██║██╔══██║██║░░╚██╗██╔══╝░░██╔══██╗",
    "██████╦╝╚██████╔╝██║░░██║██████╔╝██████╔╝██║░░██║╚██████╔╝███████╗██║░░██║",
    "╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═════╝░╚═════╝░╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝",
    ""
    ]
    for elm in bursdager:
        print(elm)


kjør = True
#  programmet kjører så lenge kjør er True, den blir kun false viss brukeren
# taster 4. Brukeren velger funksjon ut fra hvilken input den gir, 1-4.
while kjør == True:
    tomSkjerm()
    velkommen()
    print("*** Hva vil du gjøre? ***")
    print("1. Legg til bursdag")
    print("2. Finn bursdag")
    print("3. Skriv ut alle bursdager")
    print("4. Avslutt")

    valg = input(">")

    if valg == "1":
        leggTil()
    elif valg == "2":
        finnBursdag(input("Hvem sin bursdag vil du finne? \n>").lower())
    elif valg == "3":
        printAlle()
    elif valg == "4":
        kjør = False
    else:
        print("Tast inn 1, 2, 3 eller 4.")
