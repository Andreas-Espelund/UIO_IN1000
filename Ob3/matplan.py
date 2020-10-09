'''
Dette programmet lar brukeren skrive inn et navn på en beboer ved et sykehjem
og får printet deres matplan viss de er registrert i systemet. Jeg har også lagt
til en funksjon som lar brukeren legge til en beboer dersom han/hun ikke er
i systemet.
'''

# Ordboken matplan inneholder navn på beboerene ved sykehjemmet og hva de skal
# spise til frokost,lunsj og middag.
matplan = {
'Kari':['brød','gryterett','pølser'],
'Geir':['grøt','egg','suppe'],
'Simon':['frukt','potetstappe','kake'],
'Ole':['salat','svele','pudding']
}
# funksjonen hentMatplan ber om navnet på en beboer og lagrer det i variablen navn.
def hentMatplan():
    for navn in matplan:
        print(navn)
    navn =input("Velg beboer: ").capitalize()
    #IF-testen sjekker om brukeren har skrivd inn et navn som er i matplan.
    #viss den er sann, printes denne beboerens matplan ut til terminalen.
    if navn in matplan:
        print(matplan[navn])
    else:
        #Dersom IF er false, er det oppgitte navnet ikke i ordboken og
        #det blir printet at vedkommende ikke er registrert.
        print(f'{navn} finnes ikke i vårt register.')
        #brukeren får valg om å legge til beboeren i registeret
        add = input(f'Ønsker du å legge til {navn}? (ja/nei)').lower()

        #Her kan brukeren velge om den vil legge til en ny beboer
        #Ja kaller på funksjon leggTilBeboer, nei avslutter programmet.
        done = False
        while done == False:
            if add == 'ja':
                leggTilBeboer(navn)
                hentMatplan()
                done = True
            elif add == 'nei':
                print(f'{navn} blir ikke lagt til.')
                done = True
            else:
                add = input(f'Ønsker du å legge til {navn}? (ja/nei)').lower()


#leggTilBeboer legger til beboeren sitt navn og måltider i matplan ordboken.
def leggTilBeboer(navn):
    matListe = []
    matListe.append(input(f'Hva skal {navn} spise til fokost?'))
    matListe.append(input(f'Hva skal {navn} spise til lunsj?'))
    matListe.append(input(f'Hva skal {navn} spise til middag?'))
    matplan[navn] = matListe
#Jeg kaller på funksjonen hentMatplan.
hentMatplan()

"""
Oppgave 3
a.
For å lagre Brukernavn på alle IN1000 studentene ville jeg brukt en liste siden
den bare skal inneholde en verdi per person. Men om både navn og brukernavn
skulle lagres ville jeg brukt en ordbok siden hvert brukernavn er tilknyttet
en student sitt fulle navn.
b.
For å lagre alle brukernavn og poeng på innlevering 3 ville jeg brukt en ordbok
siden hver key er et brukernavn som er mappa til valuen som er poeng.
c.
For å lagre alle lottovinnerene i år(kun navn), ville jeg brukt en liste
siden vi kun skal lagre navn uten noe annen verdi som er tilknyttet.
d.
For å lagre all mat noe gjest er allergisk mot ville jeg brukt en mengde.
Dette er fordi en mengde vil da gi en oversikt over en av hver av matvarene
som folk har allergi mot. Da kan man ganske lett finne ut hva som ikke skal på
menyen ved å se på printen av denne mengden.
"""
