'''
Dette programmet har en nøstet liste som inneholder 3 lister som hver inneholder
5 steder, klesplagg og avreisedatoer. Brukeren får legge inn elementene i
listene og velger til slutt en indeks for hva som skal printes.
'''

# sjekkStr passer på at brukerinput blir bokstaver.
# Denne blir brukt for steder og klesplagg
def sjekkStr(inp):
    while inp.isalpha()==False:
        inp = input("Bruk kun bostaver: ")
    return inp.capitalize()

# sjekkDato passer på at brukeren oppgir gydlig dato og returnerer den formatert
def sjekkDato(inp):
    sjekka = False
    while sjekka == False:
        if (inp.isdigit() == True) and (len(inp) == 4):
            dag = inp[0:2]
            mnd = inp[2:4]

            if int(dag) in range(1,32) and int(mnd) in range(1,13):
                # print(dag, mnd)
                sjekka = True
            else:
                inp= input("Skriv inn en gyldig dato. (DDMM): ")
        else:
            inp= input("Skriv inn dato. Kun tall, fire siffer. (DDMM): ")

    formatertDato = dag+"."+mnd
    return formatertDato

# Listene er tomme, brukeren skal selv legge til veridene i de etterpå
steder = []
klesplagg = []
avreisedatoer = []

# indeksen i gjør at hver for løkke går 5 ganger
i = 0

# for løkken tar et reisemål som input, sjekker at det er bokstaver og legger
# det til i steder.
print("***Legg til dine reisemål***")
for i in range(5):
    reisemaal = sjekkStr(input("Skriv inn reisemaal: "))
    steder.append(reisemaal)

# for løkken spør om klesplagg, sjekker at det er bokstaver og legger de til
# i klesplagg.
print("***Legg til dine klesplagg***")
for i in range(5):
    plagg = sjekkStr(input("Skriv inn klesplagg: "))
    klesplagg.append(plagg)

# denne for løkken ber om dato, sjekker at datoen er gydlig og så legger den til
# i listen avreisedatoer
print("***Legg til dine avreisedatoer***")
for i in range(5):
    dato = input("Skriv inn dato (DDMM): ")
    avreisedatoer.append(sjekkDato(dato))
# listen reiseplan er en nøstet liste som inneholder listene steder,
# klesplagg og avreisedatoer
reiseplan = [steder, klesplagg, avreisedatoer]

# for løkken printer ut hver liste i reiseplan en etter en.
for elm in reiseplan:
    print(elm)

# i denne while løkken skal brukeren skrive inn to indekser i1 og i2.
# Desse velger hvilket element fra hvilken liste som skal printes.
# Dersom brukeren skriver inn ugyldig input får den beskjed om det.
verified = False
while verified == False:
    i1 = input("Skriv inn tall mellom 0 og 2: ")
    i2 = input("Skriv inn tall mellom 0 og 4: ")
    if i1.isdigit() and i2.isdigit():
        i1 = int(i1)
        i2 = int(i2)
        if i1 in range(len(reiseplan))  and i2 in range(len(steder)):
            print(reiseplan[i1][i2])
            verified = True
        else:
            print("Ugyldig input!")
    else:
        print("Ugyldig input!")
