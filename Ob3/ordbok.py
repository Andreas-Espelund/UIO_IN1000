'''
Dette programmet lar brukeren legge til to matvarer med pris til en prisliste
som allerede har matvarer i seg. Så printer den ut prislisten.
'''

#Jeg lager en ordbok og kaller den prisliste
prisliste = {
'melk': 14.90,
'brød': 24.90,
'yoghurt': 12.90,
'pizza': 39.90
}
#Jeg skriver ut prislisten med print funksjonen

#sjekkStr lar brukeren kun skrive inn boksaver som vare
def sjekkStr(vare):
    sjekk = vare.isalpha()
    while sjekk == False:
            vare = input("Hvilken vare vil du legge til? (Kun bokstaver!) \n>")
            sjekk = vare.isalpha()
    return vare

#sjekkFloat lar brukeren kun skrive inn tall som pris
def sjekkFloat(pris):
    sjekka = False
    while sjekka == False:
        try:
            floatPris = float(pris)
        except:
            pris = input("Hva koster den? (Kun tall!) \n>")
        else:
            sjekka = True
    return floatPris


# Brukeren skal legge til to nye varer med navn og pris, så da lager jeg en
# for-løkke som går to ganger. Jeg lager variablen i og gir den verdien 0.
i = 0
for i in range(2):
    #jeg lagrer brukerens input i to variabler, vare og pris. Så legger jeg disse
    #til ordboken med .update(). Så øker jeg verdien på i med 1.
    vare = sjekkStr(input("Hvilken vare vil du legge til? \n>"))
    pris = sjekkFloat((input("Hva koster den? \n>")))
    prisliste.update({vare:pris})
    i += 1

#Til slutt printer jeg prislisten til terminalen
# print(prisliste)


for elm in prisliste:
    spacer = 10*" "-int(len(elm))*" "
    print(elm,"koster",spacer,prisliste[elm])
