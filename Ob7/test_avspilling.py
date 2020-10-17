from sang import Sang
from spilleliste import Spilleliste

#eg lagar to nye objekter
adagio = Sang("Albinoni","Adagio","adagio.wav")
ode = Sang("Beethoven","Ode to joy","ode_to_joy.wav")

#eg lagar spelelista minListe
minListe = Spilleliste("Mine Favorittsanger")

#sangobjekta adagio og ode blir lagt til
minListe.leggTilSang(adagio)
minListe.leggTilSang(ode)

#sangane i spelelista blir avspelt
minListe.spillAlle()