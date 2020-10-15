'''
Dette programmet leser inn filer med temperaturdata for ulike datoer, og
printer statistikk om fra denne dataen til terminalen og til fil.
'''

#filTilOrdbok tar filnavn som parameter og returnerer en ordbok
def filTilOrdbok(filnavn):

    fil = open(filnavn)
    ordbok ={}
    for linje in fil:
        biter = linje.split(",")
        dato = biter[0]
        temp = float(biter[1])
        ordbok[dato] = temp

    return ordbok

#sammenlding ser om noen av datoene i filen har høyere temperatur enn
#datoene i ordboken, til slutt returnerer den en oppdatert ordbok.
def sammenlign(ordbok,filnavn):
    fil = open(filnavn)
    for linje in fil:
        biter = linje.split(",")
        dato = biter[0]
        dag = biter[1]
        temp = float(biter[2].strip("\n"))
       #dersom den innleste temperaturern for en måned er større enn i ordboken
       #printes det varmerekord til terminalen og ordboken oppdateres.
        if temp > ordbok[dato]:
            print(f'Ny varmerekord den {dag}.{dato}: {temp} grader Celcius.')
            print(f'(gammel rekord var {ordbok[dato]} grader Celcius.)')
            ordbok[dato] = temp
    return ordbok

#utskriftTilFil tar en ordbok og et filnavn som parameter, og skriver elementene
#i ordboken linje for linje til en fil med oppgitt filnavn.
def utskriftTilFil(ordbok,filnavn):
    fil = open(filnavn, "w")
    for dato in ordbok:
        fil.write(dato)
        fil.write(",")
        fil.write(str(ordbok[dato]))
        fil.write("\n")
    fil.close()

#varmebolge sjekker om det er varmebolger i filen(5+ dager med over 25 grader)
#den skriver ut tidsrommet for varmebolgene.
def varmebolge(filnavn):
    fil = open(filnavn)
    liste=[]
    #for loopen leser inn data fra filen og lager en nøstet liste.
    #hovedlisten inneholder lister med dato og tilhørende temperatur
    for linje in fil:
        linje = linje.strip("\n")
        biter = linje.split(",")
        dato = biter[1]+"."+biter[0]
        temp = float(biter[2])
        verdier =[dato,temp]
        liste.append(verdier)

    #while løkken går lengden av listen ganger -6, det er fordi for hver i
    #verdi, sjekker løkken 5 verdier fram, og -1 til fordi i begynner som 0.
    #dette er for å unngå at vi går utenfor index rangen til listen.
    i = 0
    while i < (len(liste)-6):
        j = 0
        #while løkken sjekker hvor mange sammenhengende dager framover som er
        #over 25 grader.
        while liste[i+j][1] > 25:
            j +=1
        start = liste[i][0]
        slutt = liste[i+j][0]
        #dersom perioden var over 5 dager, var det en varmebolge og det blir
        #printet til terminal.
        if j > 5:
            print("varmebolge fra",start, "til",slutt)
            i +=j-1

        i +=1

#hovedprogram kaller på funksjonene og metodene i programmet
def hovedprogram():

    maksTempPerMnd = filTilOrdbok("max_temperatures_per_month.csv")
    print("Gjeldende makstemperaturer for hver måned:")
    print(maksTempPerMnd)
    print("")

    varmerekorder = sammenlign(maksTempPerMnd,"max_daily_temperature_2018.csv")
    print("")
    print("Oppdaterte varmerekorder per maaned:")
    print(varmerekorder)

    utskriftTilFil(varmerekorder,"oppdaterteVarmedata.csv")

    print("")
    print("Varmebølger:")
    varmebolge("max_daily_temperature_2018.csv")

#til slutt et kall på hovedprogram
hovedprogram()
