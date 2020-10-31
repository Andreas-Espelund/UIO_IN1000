class Spillebrett:
    def __init__(self):
        self._rutenett = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

    def finnNabo2(self,rad,kolonne):
        #jg ser på rad og kolonne som koordinater på et kart
        #mainX og mainY, er hovedcellen sine koordinater
        mainX = rad
        mainY = kolonne
        naboer = []

        #eg iterer gjennom alle cellene i rutenettet og legger cellen til
        #naboer dersom den har en tilstøtende koorinat
        y=0
        for rad in self._rutenett:
            x = 0

            for elm in rad:
                #her kunne eg brukt and istedenfor to ekstra if setningar,
                if (x==mainX) or (x==mainX+1) or (x==mainX-1):
                    if (y==mainY) or (y==mainY+1) or(y==mainY-1):
                        if not ((x==mainX) and (y==mainY)):
                            naboer.append(elm)

                x += 1
            y += 1

        return naboer

    def finnNabo(self,rad,kolonne):
        naboer= []
        grenseK = len(self._rutenett[0]) - 1
        grenseR = len(self._rutenett) - 1
        print("grenser",grenseK, " : ",grenseR)

        for x in range(kolonne-1,kolonne+2):
            for y in range(rad-1,rad+2):
                if (0 <= x <= grenseK) and (0 <= y <= grenseR) and not(x==kolonne and y==rad):
                    naboer.append(self._rutenett[x][y])

        return naboer



    def nett(self):
        return self._rutenett


    def testNabo(self):
        for list in self._rutenett:
            for elm in list:
                if len (str(elm)) == 1:
                    elm = str(elm)+" "
                print(str(elm)+" ",end="")
            print()
        print("")
        print("-----------------------------")
        for i in range(len(self._rutenett)):
            for j in range(len(self._rutenett[0])):


                print(self._rutenett[i][j]," : ",self.finnNabo(i,j))

                print(self._rutenett[i][j]," : ",self.finnNabo2(i,j))
                print("-----------------------------")


brett = Spillebrett()
brett.testNabo()
