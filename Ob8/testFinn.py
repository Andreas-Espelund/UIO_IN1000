grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]



def finnNabo(rad,kolonne):
    naboer= []
    maxR = 3
    maxK = 3
    for i in range(rad-1,rad+2):
        for j in range(kolonne-1,kolonne+2):
            if (0 <= i) and (0 <= j) and not ((i==rad) and (j==kolonne)):

                try:
                    naboer.append(grid[i][j])
                except:
                    pass
    return naboer

for list in grid:
    for elm in list:
        if len (str(elm)) == 1:
            elm = str(elm)+" "
        print(str(elm)+" ",end="")
    print()
print("")
print("-----------------------------")
for i in range(len(grid)):
    for j in range(len(grid[0])):


        print(grid[i][j]," : ",finnNabo(i,j))
        print("-----------------------------")
