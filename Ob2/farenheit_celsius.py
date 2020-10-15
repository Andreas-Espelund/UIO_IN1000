'''
Dette progrgammet tar inn brukerinput som en temperatur i farenheit, regner
om denne til celsius og printer temperaturen i celsius og farenheit.
'''
# Funksjonen verifiserInput sjekker om brukeren sin input er et tall
def verifiserInput(inp):
    #global nøkkelordet gjør at variablen farenheit kan brukes utenfor funksjonen
    global farenheit
    #variablen ver er False og indikerer at brukerinputen ikke er verifisert
    ver = False
    #while løkken går så lenge ver er False.
    while ver == False:
        #Jeg bruker en try,except,else statement for å sjekke input-en
        try:
            #Den prøver først å gjøre inputen om til et flyttall.
            #Dersom inputen er noe annet en tall, går den til except
            #Dersom inputen er tall, går den til else
            farenheit = float(inp)
        except:
            #Her får brukeren beskjed om å skrive inn temperaturen på nytt
            print("Ugyldig inntasting! Skriv inn et tall.")
            inp = input("Oppgi temperatur i farenheit: ")
        else:
            #Ver blir satt til True og løkka stopper
            ver = True

#Først lagrer jeg brukeren sin input i variablen inp
inp = input("Oppgi temperatur i farenheit: ")
#Deretter kaller jeg på verifiserInput med inp som parameter
verifiserInput(inp)
#Så regner jeg om temperaturen til celsius
celsius = (farenheit-32)*5/9
'''
Jeg bruker print funksjonen til å printe variablene celsius og farenheit
til terminalen. Jeg bruker (:.2f) formatering på celsius variablen for
å runde den av til 2 desimaler.
'''
print(f'Temperaturen er {farenheit} farenheit.')
print(f'Temperaturen er {celsius:.2f} grader celsius.')
