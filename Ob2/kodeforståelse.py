'''
1.
Dette er ikke lovlig kode fordi print setningen på linje 16 prøver å
legge sammen en streng og et heltall.
2.
Vi kommer til å få en feilmelding på linje 16 om at typen objekter 'int' og 'str'
ikke er støttet.
Løsning:
For å løse dette slik at programmet kan kjøre må vi skrive print setningen slik:
    print(f'{b} Hei')
'''

a = input ( "Tast inn et heltall! " )
b = int ( a )
if b < 10 :
    print ( b + "Hei!" )
