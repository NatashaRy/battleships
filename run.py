HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
GUESS_BOARD = [["_"] * 8 for x in range(8)]

letters_to_numbers = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}


def print_board(board):
    """
    Printing the game boards.
    A-H as a headlines for columns and 1-8 marking the row numbers.
    """
    print("  A B C D E F G H")
    row_num = 1
    for row in board:
        print(f"{row_num}|{'|'.join(row)}|")
        row_num += 1

print("Welcome to Battleships!")
name = input("What is your name: ")
print("Start the game by placing your ships on the board.\n")
print_board(HIDDEN_BOARD)

ships = {
    "Battleship": {"size": 4, "char":'B', "position": None, "orientation": None},
    "Submarine": {"size": 3, "char":'S', "position": None, "orientation": None},
    "Patrol_boat": {"size": 2, "char":'P', "position": None, "orientation": None},
}

def is_valid_placement(position, orientation, ship_size):
    """
    Convert letter to number and check if the position is valid.
    """
    col = ord(position[0]) + ord('A') + 1
    row = int(position[1:])

    if orientation == 'H' and col + ship_size > 7:
        return False
    if orientation == 'V' and row + ship_size > 7:
        return False

    return True

def get_ship_placement(ship_name, ship_size):
    """
    Let the player choose a starting position and orientation for a ships.
    Checks if the placement is valid.
    """
    print("\nShip sizes (1 x): Battleship: 4, Submarine: 3, Patrol_boat: 2")
    while True:
        position = input(f"Enter starting position for {ship_name} (e.g. A3): ").upper()
        orientation = input("Enter orientation (H for horizontal, V for vertical): ").upper()

        if is_valid_placement(position, orientation, ship_size):
            return position, orientation
        else:
            print("Invalid placement, please try again.")

for ship, details in ships.items():
    position, orientation = get_ship_placement(ship, details["size"])
    details["position"] = position
    details["orientation"] = orientation

# Place computers ships

# Get ship location - Ask user for row and column

# Count hit ships

# print("How to play: \n")
