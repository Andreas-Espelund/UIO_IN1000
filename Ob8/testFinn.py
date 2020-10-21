def finnNabo(rad,kolonne):
    mainX = rad
    mainY = kolonne
    naboer = []

    y=0
    for rad in grid:
        x = 0
        for elm in rad:
            if (x==mainX) or (x==mainX+1) or (x==mainX-1):
                if (y==mainY) or (y==mainY+1) or(y==mainY-1):
                    if not ((x==mainX) and (y==mainY)):
                        naboer.append(elm)

            x += 1
        y += 1

    return naboer

grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

liste = finnNabo(0,0)

print(liste)
