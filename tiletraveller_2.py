import random

seed = int(input("Input seed: "))
random.seed(seed)

# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
        
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions

def play_one_move(col, row, valid_directions, if_true):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = random.choice(["n", "e", "s", "w"])
    print("Direction: {}" .format(direction))
    direction = direction.lower()
    
    if not direction in valid_directions:
        print("Not a valid direction!")
        if_true = False
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
        if_true = True
    return victory, col, row, if_true

def leaver(row, col, coins, if_ture):
    if col == 1 and row == 2 and if_true == True:
        pull = random.choice(["y", "n"])
        print("Pull a lever (y/n): {}" .format(pull))
        if pull == "y":
            coins += 1
            print("You received 1 coin, your total is now {}." .format(coins))
    
    elif col == 2 and row == 2 and if_true == True:
        pull = random.choice(["y", "n"])
        print("Pull a lever (y/n): {}" .format(pull))
        if pull == "y":
            coins += 1
            print("You received 1 coin, your total is now {}." .format(coins))
    
    elif col == 2 and row == 3 and if_true == True:
        pull = random.choice(["y", "n"])
        print("Pull a lever (y/n): {}" .format(pull))
        if pull == "y":
            coins += 1
            print("You received 1 coin, your total is now {}." .format(coins))
    
    elif col == 3 and row == 2 and if_true == True:
        pull = random.choice(["y", "n"])
        print("Pull a lever (y/n): {}" .format(pull))
        if pull == "y":
            coins += 1
            print("You received 1 coin, your total is now {}." .format(coins))
    return coins
        

# The main program starts here
while True:
    victory = False
    row = 1
    col = 1
    if_true = True
    coins = 0
    moves = 0

    while not victory:
        valid_directions = find_directions(col, row)
        coins = leaver(row, col, coins, if_true)
        print_directions(valid_directions)
        victory, col, row, if_true = play_one_move(col, row, valid_directions, if_true)
        moves += 1

    print("Victory! Total coins {}. Moves {}." .format(coins, moves))
    play_again = input("Play again (y/n): ")
    if play_again == "y":
        continue
    else:
        break
