#Leikður er í maze með 9 reitum, það er takmarkað hvernig hann getur hreyft sig 
#á hvernjum stað sem hann er á fær hann upp hvert hann getur hreyft sig "You can travel: "
# þarf að velja einn möguleika (n,e,s,w), ef hann velur eitthvað sem er ekki í boði þá fær hann "Not a valid direction!"
#   7   8   9
#   4   5   6
#   1   2   3

def tile_travel(inpitið?)
    tile_1 = "n" or "N"
    tile_2 = "n" or "N"
    tile_3 = "n" or "N" #Victory 
    tile_4 = "n" or "N" or "s" or "S" or "e" or "E"
    tile_5 = "s" or "S" or "w" or "W"
    tile_6 = "n" or "N" or "s" or "S"
    tile_7 = "s" or "S" or "e" or "E"
    tile_8 = "e" or "E" or "w" or "W"
    tile_9 = "s" or "S" or "e" or "E"

val = 1 
while val:
    if 