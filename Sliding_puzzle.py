
#þegar notandi stimplar inn 0 þá hættir hann 
# inntak = 5 3 13 7 14 10 0 11 1 4 6 8 12 9 2 15
#4 tölur í línu 
# 0 er autt 
#talan sem hann skimplar inn fer í auða reytin og reiturinn sem hun kom úr verður auður

# Constants
DIM = 4 # dimension of the board DIMxDIM
EMPTYSLOT = 0
QUIT = 0

def initialize_board():
    ''' Creates the initial board according to the user input.
    The board is a list of lists.
    The list contains DIM elements (rows), each of which contains DIM elements (columns)'''
    numbers = input().split()
    numbers = [int(number) for number in numbers]
    puzzle_board = []
    index = 0
    for _ in range(DIM):
        row = numbers[index:index + DIM]
        index += DIM
        puzzle_board.append(row)

    return puzzle_board
    

def display(puzzle_board):
    ''' Display the board, printing it one row in each line '''
    print()
    for i in range(DIM):
        for j in range(DIM):
            if puzzle_board[i][j] == EMPTYSLOT:
                print("\t", end="")
            else:
                print(str(puzzle_board[i][j]) + "\t", end="")
        print()
    print()


def moves(puzzle_board):

    move = input()

    for number in puzzle_board:
        print(number)
        # if number == move:
        #     number = EMPTYSLOT 

    


puzzle_board = initialize_board()
print(puzzle_board)
dis = display(puzzle_board)
mamma = moves(puzzle_board)