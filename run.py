#Game boards
HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
GUESS_BOARD = [['_'] * 8 for x in range(8)]

letters_to_numbers = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}

def print_board(board):
    """
    Printing the game boards.
    """
    print ('  A B C D E F G H')

    row_num = 1
    for row in board:
        print(f"{row_num}|{'|'.join(row)}|")
        row_num += 1 

#Create ships

#Get ship location - Ask user for row and column

#Count hit ships




#print("Welcome to Battleships!")
#print("Board size: , numbers of ships: \n")
#print("How to play: \n")
#name = input("What is your name: ")