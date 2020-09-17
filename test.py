#Leikður er í maze með 9 reitum, það er takmarkað hvernig hann getur hreyft sig 
#á hvernjum stað sem hann er á fær hann upp hvert hann getur hreyft sig "You can travel: "
# þarf að velja einn möguleika (n,e,s,w), ef hann velur eitthvað sem er ekki í boði þá fær hann "Not a valid direction!"
#   7   8   9
#       _
#   4   5 |  6
#  
#   1  | 2 | 3


row1 = "ES/EW/WS/"              #Allar mögulegar leiðir 
row2 = "NES/WS/NS/"
row3 = "N/N/V/"

indexY = 0              #Y-ás
indexX = 0              #X-ás

def position(indexX,row):
    counter = -1
    idex1 = 0 
    last = 0                    #seinasta /
    for i in row:
        if i == "/":
            counter += 1
            if counter == indexX:
                return row[last:idex1]        #reyna finna næsta /
            else:
                last = idex1
        idex1 += 1                             #testa, print(position(indexX,getRox(indexY, rox1, rox2, rox3))) --> fá reit 1 

def canMove(indexX,row, directions):
    stadus = position(indexX,row)
    if directions in stadus:
        return True
    else:
        return False 

#vil vita hvert ég er að fara og x og y index 

def changeidex1(directions, indexX, indexY):
    if directions == "N" or "n":
        indexY += 1
        return indexY, indexX
    elif directions == "E" or "e":
        indexX += 1
        return indexY, indexX
    elif directions == "S" or "s":
        indexY -= 1
        return indexY, indexX
    elif directions == "W" or "w":
        indexX -= 1
        return indexY, indexX


def getRow(indexY,row1,row2,row3):
    if indexY == 0:
        return row3
    elif indexY == 1:
        return row2
    elif indexY == 2:
        return row1

#láta notendann vita hvað hann getur gert

def printDriections(row):
    string = ""
    for x in row:
        if x == "N" or "n":
            string += "(N)orth or "
        if x == "E" or "e":
            string += "(E)ast or "
        elif x == "S" or "s":
            string += "(S)outh or "
        elif x == "W" or "w":
            string += "(W)est or "   
    string = string[:-4] + "."                 #taka or, 2 space og 2 starfi, og setja punkt
    return string 

#leggja grunninn fyrir hvernig forritið virkar 

val = True

while val: 
    possible_moves = printDriections(position(indexX,getRow(indexY, row1, row2, row3)))
    if position(indexX, getRow(indexY, row1, row2, row3)) == "V":
        print("Victory!")
        break 
    current = getRow(indexY, row1, row2, row3)
    print(f"You can travel: {possible_moves}")
    directions = input("Directions: "
    if canMove(indexX, current, directions):
        indexY indexX = changeidex1(directions, indexX, indexY)
    else:
        print("Not a valid Direction")
