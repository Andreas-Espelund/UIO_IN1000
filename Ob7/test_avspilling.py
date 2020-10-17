from sang import Sang
from spilleliste import Spilleliste

adagio = Sang("Albinoni","Adagio","adagio.wav")
ode = Sang("Beethoven","Ode to joy","ode_to_joy.wav")

minListe = Spilleliste("Mine Favorittsanger")
minListe.leggTilSang(adagio)
minListe.leggTilSang(ode)

minListe.spillAlle()

