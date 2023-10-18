import random

HIDDEN_BOARD = [[" "] * 8 for _ in range(8)]
GUESS_BOARD = [[" "] * 8 for _ in range(8)]
PLAYERS_BOARD = [[" "] * 8 for _ in range(8)]


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


SHIPS = {
    "BATTLESHIP": {"size": 4, "char": "B", "position": None, "orientation": None},
    "SUBMARINE": {"size": 3, "char": "S", "position": None, "orientation": None},
    "PATROL_BOAT": {"size": 2, "char": "P", "position": None, "orientation": None},
}

def create_computer_ships(board):
    """
    Create computer's ships on board randomly, placement marked with ships character.
    Checks the size of the ship to verify that placement is valid.
    """
    for ship, details in SHIPS.items():
        ship_char = details["char"]
        ship_size = details["size"]

        placed = False
        while not placed:
            orientation = random.choice(["H", "V"])
            if orientation == "H":
                ship_row = random.randint(0, 7)
                ship_column = random.randint(0, 7 - ship_size)
            else:
                ship_row = random.randint(0, 7 - ship_size)
                ship_column = random.randint(0, 7)
            if orientation == "H":
                if all(
                    [board[ship_row][ship_column + i] == " " for i in range(ship_size)]
                ):
                    for i in range(ship_size):
                        board[ship_row][ship_column + i] = ship_char
                    placed = True
            else:
                if all(
                    [board[ship_row + i][ship_column] == " " for i in range(ship_size)]
                ):
                    for i in range(ship_size):
                        board[ship_row + i][ship_column] = ship_char
                    placed = True

def place_players_ships(board):
    """
    Let player place their ships on board, by choosing starting position and orientation.
    Placement marked with ships character.
    """
    for ship, details in ships.items():
        ship_char = details["char"]
        ship_size = details["size"]

        print_board(HIDDEN_BOARD)
        print("Start the game by placing your ships on the board.\n")
        print("Ship sizes (1 x): Battleship: 4, Submarine: 3, Patrol_boat: 2")
        while True:
            position = input(
                f"Please enter starting position for {ship} (e.g. A1): "
            ).upper()
            orientation = input(
                f"Enter orientation (H for horizontal, V for vertical): "
            ).upper()

            placed_ship = position[0] + ord("A") - 1
            row = int(position[1:])

            if orientation == "H" and placed_ship + ship_size > 7:
                print("Please enter a valid orientation.")
                return False
            elif orientation == "V" and placed_ship + ship_size > 7:
                print("Please enter a valid orientation.")
                return False
            else:
                return position, orientation

def players_guess():
    """
    Convert letters to numbers, get location of ships.
    Limit player to only enter numbers for row and letters for column.
    Returns row and column of location of input.
    """
    letters_to_numbers = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
    }

    row = input('Please enter a ship row, 1-8: ')
    while not row.isdigit() or row not in "12345678":
        row = input("Please enter a vaild ship row, 1-8: ")

    column = input('Please enter a ship column, A-H: ').upper()
    while not column.isalpha() or column not in "ABCDEFGH":
        column = input("Please enter a valid ship column, A-H: ").upper()

    return int(row) -1, letters_to_numbers[column]


def count_hit_ships(board):
    ""
    count = 0
    for row in board:
        for cell in row:
            if cell in [details["char"] for details in SHIPS.values()]:
                count += 1

print("Welcome to Battleships!")
name = input("What is your name: ")
while not name.isalpha():
    name = input("Enter your name (letter only): ")

char_to_ship = {details["char"]: ship for ship, details in SHIPS.items()}

create_computer_ships(HIDDEN_BOARD)
while True:
    print_board(GUESS_BOARD)
    row, column = players_guess()
    if GUESS_BOARD[row][column] == "X":
        print("You already guessed that, try again.\n")
    else:
        HIT_SHIP = None
        for ship, details in SHIPS.items():
            if HIDDEN_BOARD[row][column] == details["char"]:
                HIT_SHIP = ship
                break

    if HIT_SHIP:
        print(f"You hit the {HIT_SHIP}!")
        GUESS_BOARD[row][column] = HIDDEN_BOARD[row][column]
    else:
        print("Miss!\n")
        GUESS_BOARD[row][column] = "X"
