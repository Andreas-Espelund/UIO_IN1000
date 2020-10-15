#Variabelen navn_a får verdien fra brukeren med input()
#Deretter blir ei helsing printa med brukerens input (navn)
navn_a = input("Skriv inn ditt navn: ")
print("Hei!", navn_a,"!")

#Eg lagar to variablar med verdiane 20 og 17
alder = 20
favorittall = 17
#Eg printar desse variablane til terminalen
print(alder)
print(favorittall)
#Eg lagar en ny variabel som har vedien til differansen mellom
#dei forrige variablane
differanse = alder - favorittall
print("Differanse :" ,differanse)

# Eg lagar en ny variabel navn_b som brukaren skal gi en verdi med input()
# deretter lagar eg enda en variabel 'sammen' som inneheld navn_a og navn_b.
navn_b = input("Skriv inn enda et navn: ")
sammen = navn_a + navn_b
#Eg printar ut variablen 'sammen'
print(sammen)
#Sidan sammen var ei sammenslåing av to navn, legg eg til " og " mellom navna
#for å skille dei.
sammen = navn_a +" og "+ navn_b
#Deretter printar eg sammen på nytt men no er det mykje lettare for
#brukeren å lese.
print(sammen)
