'''
Dette programmet bruker modulen ezgraphics for å tegne sirkler i et
grafisk vindu.
'''

from ezgraphics import GraphicsWindow

win = GraphicsWindow()
win.setTitle("Kult sirkelprogram")
can = win.canvas()
can.setBackground(50,125,250)


count = 0
x_pos = 10
stoerrelse = 50
# While løkken går 9 ganger, og tegner en sirkel for hver gang.

#jeg la til listen col, med ulike verdier for fargene R,G,B for litt ekstra spice
col=[255,0,0]
while count < 9:
    can.setOutline(col[0],col[1],col[2])
    can.drawOval(x_pos, 100, stoerrelse, stoerrelse)
    #Størrelse øker med 5 for hver gang, x_pos øker med 20
    count +=1
    x_pos += 20
    stoerrelse += 5
    #Fargene til hver sirkel endres
    col[0]-=25
    col[1]+=25
win.wait()
#
