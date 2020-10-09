'''
Først defineres minFunksjon som ikke skal ta imot noen paramtere,
så defineres hovedprogram som heller ikke tar imot paramter.
hvoedprogram blir kallet på. Det blir opprettet en variabel 'a' med verdien 42 og
en variabel 'b' som får verdien 0. b blir printet til terminalen. Verdien til
variabel 'b' endret til verdien til variabel 'a' som er 42.
a verdien blir endret til resultatet av minFunksjon, så funksjonen minFunksjon
blir kalt på:

for løkken går når x har verdi fra 0 til 2. x er først 0, løkka gjør følgende:
    Variabelen 'c' blir opprettet med verdien 2
    'c' blir printet til terminalen
    'c' øker med 1
    Variabelen 'b' blir opprettet med vedien 10.

    'b' blir forsøkt økt med verdien av 'a', men den er en lokal variabel i
    funksjonen hovedprogram, så den er ikke tilgjengelig i funksjonen
    minFunksjon. Den er altså ikke global eller definert i minFunksjon.
    vi vil altså få en name error i linje 28 (b+=a)
'''

def minFunksjon ():
    for x in range ( 2 ):
        c = 2
        print ( c)
        c += 1
        b = 10
        b += a    # her vil feilen oppstå
        print ( b )
    return ( b )

def hovedprogram():
    a = 42
    b = 0
    print ( b )
    b = a
    a = minFunksjon ()
    print ( b )
    print ( a )

hovedprogram()
