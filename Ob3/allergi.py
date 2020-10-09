'''
1. Lag en ordbok med deltakere på et arrangement og hvilke allergier
   de har.
2. Lag så en ordbok med matvarer og allergenene de inneholder.
3. Definer en funksjon/metode som kan avgjøre hvilke retter som bør utelates
   fra menyen.
4. Skriv ut en meny som inneholder kun matretter som alle kan spise.
'''

#Ordboken deltakere inneholder navn på deltaker og allergier.
deltakere = {
'lisa':['gluten','laktose'],'ole':['egg','laktose'],
'georg':['gluten'],'samuel':['gluten','tomat']
}
#Ordboken matretter inneholder type matrett og innhold/allergener
matretter = {
'burger': ['gluten','kjøtt'],'kake':['laktose','gluten'],
'eggerøre' : ['egg'],'fisk':['omega3','laks','sitron'],
'pizza':['chilli','løk','skinke'],'baguett':['kylling','dressing'],
'tomatsuppe':['tomat','løk','chilli'],'gryterett': ['kjøtt','mais','ris']
}

# Jeg lagrer alle deltakerene sine allergener i mengden allergener
allergener = set()
for liste in deltakere.values():
    for elm in liste:
             allergener.add(elm)

# Jeg sammenligner allergenene i matretter mot mengden allergener og legger
# matrettene som deltakerene er allergiske mot i listen offMenu
offMenu = []
for retter in matretter:
    for alr in allergener:
        if alr in matretter.get(retter):
            offMenu.append(retter)

# Jeg lager en tom liste menu som jeg legger til alle meny-objektene med en
# For-løkke som itererer gjennom ordboken matretter og legger alle key'ene til
# listen menu.
menu =[]
for item in matretter:
    menu.append(item)

#Jeg bruker list comprehension for å lage en ny liste onMenu som består av
#matretter som er i menu og ikke i offMenu
onMenu = [mat for mat in menu if mat not in offMenu]

'''
alternativ måte til list comprehension
onMenu =[]
for mat in menu:
    if mat not in offMenu:
        onMenu.append(mat)
'''
#For-løkken itererer gjennom onMenu lista og printer meny objektene en etter en
#Slik at det blir lettere for brukeren å lese.
print("Meny:")
for menObj in onMenu:
    print(menObj.capitalize())
