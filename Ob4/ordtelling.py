'''
Dette programmet tar en setning som input fra brukeren og printer ut
hvor mange ord setningen består av. Den printer også hvor mange ganger hvert ord
er skrevet i setningen og lengden på ordene.
'''

# Funksjonen orlengde tar et ord som parameter og returnerer lengden til ordet.
def ordLengde(ord):
    return len(ord)

# setningTilOrdbok tar en setning som paramteret og printer lengden på setningen,
# antall av hvert ord og lengden på de ordene.
def setningTilOrdbok(setning):
    liste = setning.split()
    print(f'Det er {len(liste)} ord i setningen din.')
    ordbok = {}

    for ord in liste:
        ordbok[ord] = liste.count(ord)

    for elm in ordbok:
        if ordbok[elm] == 1:
            # Jeg lager to ulike print statements slik at det ikke blir printet
            # '1 ganger' eller '2 gang'.
            if len(elm) == 1:
                print(f"Ordet '{elm}' forekommer {ordbok[elm]} gang, og har {ordLengde(elm)} bokstav.")
            else:
                print(f"Ordet '{elm}' forekommer {ordbok[elm]} gang, og har {ordLengde(elm)} bokstaver.")

        else:
            if len(elm) == 1:
                print(f"Ordet '{elm}' forekommer {ordbok[elm]} ganger, og har {ordLengde(elm)} bokstav.")
            else:
                print(f"Ordet '{elm}' forekommer {ordbok[elm]} ganger, og har {ordLengde(elm)} bokstaver.")
# Jeg kaller på funksjonen setningTilOrdbok med brukerinput som parameter


setningTilOrdbok(input("Skriv inn en setning: \n>"))
