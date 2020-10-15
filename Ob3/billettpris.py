'''
Dette programmet bestemmer billetpris for brukeren utifra alder.
'''

#Funksjonen tallsjekk tar alderInput og sjekker om dette er et heltall og
#returnerer alder når det er godkjent input.
def tallsjekk(alderInput):
    verifisert = False
    while verifisert == False:
        try:
            alder = int(alderInput)
        except:
            alderInput = input("Vennligst oppgi alder som heltall! \n>")
        else:
            verifisert = True
    return alder

#Kontroll printer en billettpris basert på alderen som brukeren oppgir.
#Barn og pensjonister får 50% rabatt.
def kontroll():
    alderInput = input("Hvor gammel er du? \n>")
    alder = tallsjekk(alderInput)
    billettpris = 0

    if alder <= 17 or alder >= 63:
        billettpris = 30
    else:
        billettpris = 50
    print(f'Billetten koster {billettpris} kr')

#Jeg lager variablen i med verdien 0
#For-løkka går til når i er mellom 0 og 4.
i = 0
for i in range(4):
    #funksjonen kontroll blir kallet på og så øker jeg i med 1.
     kontroll()
     i += 1

'''
Oppg.6
Dersom du oppgir verdier som ikke er heltall, altså spesialtegg, bokstaver eller
desimaltall, vil prorammet avsluttes og du får en feilmelding. Eksempel:
Brukeren skriver inn: "tolv" --> ValueError
Dette har jeg fikset ved å legge til tallsjekk metoden som ikke lar brukeren
skrive inn noe annet en heltall.
'''
