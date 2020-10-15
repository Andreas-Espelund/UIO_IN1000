#Brukeren gir variablen vilHaBrus verdien ja eller nei
#Eg brukar .lower() for å sikre at all input er med små bokstavar
#Dette vil forenkle IF-setninga
vilHaBrus = input("Vil du ha brus? (ja/nei): ").lower()
#IF-setninga testar om brukeren vil ha brus
if vilHaBrus == "ja":
    print("Her har du en brus!")
#elif-setninga testar om brukeren ikkje vil ha brus
elif vilHaBrus == "nei":
    print("Den er grei.")
#else setninga blir kjørt dersom brukeren har
# gitt anna input enn 'ja' eller 'nei'
else:
    print("Det forstod jeg ikke helt.")
