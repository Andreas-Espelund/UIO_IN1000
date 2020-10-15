#Jeg lager en ny liste, kaller den tall og lagrer tallene 1,3 og 5
tall = [1,3,5]

#Jeg bruker append til å legge til tallet 6 på slutten av lista
tall.append(6)

#det første og tredje tallet blir printa
print(tall[0],tall[2])


#For løkka lar brukeren legge til 4 navn i nyListe
nyListe = []
for i in range(4):
    inp = input("Skriv inn en navn: ").lower()
    nyListe.append(inp)
    i +=1

#Brukeren får beskjed om mitt navn ble lagt til i listen over
if 'andreas' in nyListe:
    print("Du husket meg!")
else:
    print("Glemte du meg?")

# Jeg lagrer summen av tall i variablen sum
sum = sum(tall)

# Jeg looper gjennom listen og mulipliserer elementene en etter en og
#lagrer de i variablen produkt.
produkt = 1
for elm in tall:
    produkt = produkt*elm

# Jeg lager en ny liste nyeTall med variablene sum og produkt
nyeTall = [sum,produkt]
# Jeg lager en ny liste sammenTall og slår sammen listene tall og nyeTall
sammenTall = tall + nyeTall
# Så printer jeg ut listen sammenTall
print(sammenTall)

# Jeg fjerner de to siste objektene i listen sammenTall med .pop og printer den

sammenTall.pop(-1)
sammenTall.pop(-1)
print(sammenTall)
