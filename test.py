#Leikður er í maze með 9 reitum, það er takmarkað hvernig hann getur hreyft sig 
#á hvernjum stað sem hann er á fær hann upp hvert hann getur hreyft sig "You can travel: "
# þarf að velja einn möguleika (n,e,s,w), ef hann velur eitthvað sem er ekki í boði þá fær hann "Not a valid direction!"
#   7   8   9
#       _
#   4   5 |  6
#  
#   1  | 2 | 3


row1 = "ES/EW/SW/" #Allar mögulegar leiðir 
row2 = "NES/SW/NS/"
row3 = "N/N/V/"

indexY = 0  #Y-ás
indexX = 0  #X-ás

def position(indexX,row):
    counter = -1
    idx = 0
    last = 0    #seinasta /
    for i in row:
        if i == "/":
            counter += 1
            if counter == indexX:
                return row[last:idx]    #reyna finna næsta /
            else:
                last = idx
        idx += 1        #testa, print(position(indexX,getRox(indexY, rox1, rox2, rox3))) --> fá reit 1 

def canMove(indexX,row,direction):
    s = position(indexX,row)
    if direction in s:
        return True
    else:
        return False

        #vil vita hvert ég er að fara og x og y index 
def changeIdx(direction,indexY,indexX):
    if direction == "N":
        indexY += 1
        return indexY,indexX
    elif direction == "E":
        indexX += 1
        return indexY,indexX
    elif direction == "S":
        indexY -= 1
        return indexY,indexX
    elif direction == "W":
        indexX -= 1
        return indexY,indexX

def getRow(indexY,row1,row2,row3):
    if indexY == 0:
        return row3
    elif indexY == 1:
        return row2
    elif indexY == 2:
        return row1

#láta notendann vita hvað hann getur gert
def printDirections(row):
    string = ""
    for x in row:
        if x == "N":
            string += "(N)orth or "
        elif x == "E":
            string += "(E)ast or "
        elif x == "S":
            string += "(S)outh or "
        elif x == "W":
            string += "(W)est or "
    string = string[:-4] + "."  #taka or, 2 space og 2 starfi, og setja punkt
    return string


    #leggja grunninn fyrir hvernig forritið virkar 
while True:
    where_can_go = printDirections(position(indexX,getRow(indexY,row1,row2,row3)))
    if position(indexX,getRow(indexY,row1,row2,row3)) == "/V":
        print("Victory!")
        break
    current = getRow(indexY,row1,row2,row3)
    print(f"You can travel: {where_can_go}")
    direction = input("Direction: ")
    direction = direction.upper()
    if canMove(indexX,current,direction):
        indexY, indexX=changeIdx(direction,indexY,indexX)
    else:
        print("Not a valid direction!")
