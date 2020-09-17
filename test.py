row1 = "ES/EW/WS/"
row2 = "NES/WS/NS/"
row3 = "N/N/V/"

indexY = 0
indexX = 0

def position(indexX,row):
    counter = -1
    idx = 0
    last = 0
    for i in row:
        if i == "/":
            counter += 1
            if counter == indexX:
                return row[last:idx]
            else:
                last = idx
    idx += 1




def getRow(indexY,row1,row2,row3):
    if indexY == 0:
        return row3
    elif indexY == 1:
        return row2
    elif indexY == 2:
        return row1

def printDirections()