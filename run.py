import random
import re

HIDDEN_BOARD = [["_"] * 8 for _ in range(8)]
GUESS_BOARD = [["_"] * 8 for _ in range(8)]
PLAYERS_BOARD = [["_"] * 8 for _ in range(8)]
player_sunk_count = 0
computer_sunk_count = 0


def reset_game():
    """
    Resets the game and let the game boards be modified.
    """
    HIDDEN_BOARD[:] = [["_"] * 8 for _ in range(8)]
    GUESS_BOARD[:] = [["_"] * 8 for _ in range(8)]
    PLAYERS_BOARD[:] = [["_"] * 8 for _ in range(8)]
    player_sunk_count[:] = 0
    computer_sunk_count[:] = 0
    for ship, details in SHIPS.items():
        details["sunk"] = False


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
    "Battlehip": {
        "size": 4,
        "char": "B",
        "position": None,
        "orientation": None,
        "sunk": False,
    },
    "Submarine": {
        "size": 3,
        "char": "S",
        "position": None,
        "orientation": None,
        "sunk": False,
    },
    "Patrol boat": {
        "size": 2,
        "char": "P",
        "position": None,
        "orientation": None,
        "sunk": False,
    },
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
                    [board[ship_row][ship_column + i] == "_" for i in range(ship_size)]
                ):
                    for i in range(ship_size):
                        board[ship_row][ship_column + i] = ship_char
                    placed = True
            else:
                if all(
                    [board[ship_row + i][ship_column] == "_" for i in range(ship_size)]
                ):
                    for i in range(ship_size):
                        board[ship_row + i][ship_column] = ship_char
                    placed = True


def place_players_ships(board):
    """
    Let player place their ships on board, by choosing starting position and orientation.
    Limit player to only enter specific format for guess (e.g., '1A', '2B').
    Placement marked with ships character.
    """
    for ship, details in SHIPS.items():
        ship_char = details["char"]
        ship_size = details["size"]

        placed = False
        while not placed:
            print_board(board)
            print(f"\nPlacing a '{ship}' of size {ship_size} on the board.")

            position = input(
                f"Please enter starting position for {ship} (e.g., A1): "
            ).upper()
            if (
                len(position) < 2
                or position[0] not in "ABCDEFGH"
                or not position[1:].isdigit()
            ):
                print("Invalid position. Please use the format 'A1', 'C3' etc.")
                continue

            orientation = input(
                "Enter orientation (H for horizontal, V for vertical): "
            ).upper()

            column = ord(position[0]) - ord("A")
            row = int(position[1:]) - 1

            if orientation not in ["H", "V"]:
                print("Invalid orientation. Choose 'H' or 'V'.")
                continue

            if (orientation == "H" and column + ship_size > 8) or (
                orientation == "V" and row + ship_size > 8
            ):
                print("\nShip placement out of bounds, try again.\n")
                continue

            if orientation == "H":
                if all(
                    board[row][col] == "_" for col in range(column, column + ship_size)
                ):
                    for col in range(column, column + ship_size):
                        board[row][col] = ship_char
                    placed = True
                else:
                    print("Another ship is already in that position.")
            else:
                if all(board[r][column] == "_" for r in range(row, row + ship_size)):
                    for r in range(row, row + ship_size):
                        board[r][column] = ship_char
                    placed = True
                else:
                    print("Another ship is already in that position.")

            if placed:
                print(f"{ship} placed on the board.\n")
    print_board(PLAYERS_BOARD)
    print("All ships have been successfully placed!\n")


def players_guess():
    """
    Convert letters to numbers, get location of ships.
    Limit player to only enter specific format for guess (e.g., '1A', '2B').
    Returns row and column of location of input.
    """
    print(HIDDEN_BOARD)

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

    pattern = re.compile(r"^[A-Ha-h][1-8]$")

    guess = input("Please enter your guess (e.g., 'A1'): ").upper().replace("_", "")
    while not pattern.match(guess):
        guess = (
            input("Invalid input. Please enter your guess (e.g., '1A', '2B'): ")
            .upper()
            .replace("_", "")
        )

    column = guess[0]
    row = guess[1]

    return int(row) - 1, letters_to_numbers[column]


def computer_guess(board):
    """
    Let the computer randomly guess the placement of the player's ships.
    Checkes if the cell has been guessed or missed before.
    """
    column, row = random.randint(0, 7), random.randint(0, 7)
    while board[row][column] == "X" or board[row][column] == "-":
        row, column = random.randint(0, 7), random.randint(0, 7)
    return row, column


def count_char_on_board(board, char):
    """
    Count the occurrences of a character on a board.
    """
    return sum(row.count(char) for row in board)

def check_ship_sunk_player(board):
    """
    Check if the player have sunk any ships on the given board.
    Returns the name of the sunk ship or None if no ship was sunk.
    """
    for ship, details in SHIPS.items():
        char_count = count_char_on_board(board, details["char"])
        if char_count == 0 and not details["sunk"]:
            details["sunk"] = True
            return ship

def players_turn():
    """
    Players game logic.
    """
    global player_sunk_count
    print_board(GUESS_BOARD)

    while True:
        row, column = players_guess()
        if GUESS_BOARD[row][column] == "X":
            print("You already guessed that, try again.\n")
            continue
        else:
            hit_ship = None
            for ship, details in SHIPS.items():
                if HIDDEN_BOARD[row][column] == details["char"]:
                    hit_ship = ship
                    break
            if hit_ship:
                GUESS_BOARD[row][column] = HIDDEN_BOARD[row][column]
                print(f"You hit the {hit_ship}!\n")
            else:
                print("Miss!\n")
                GUESS_BOARD[row][column] = "X"
            break

    sunk_ship_by_player = check_ship_sunk_player(GUESS_BOARD)
    if sunk_ship_by_player:
        print(f"You have sunk the computer's {sunk_ship_by_player}!\n")
        player_sunk_count += 1
    return player_sunk_count


def computers_turn():
    """
    Computers game logic.
    """
    global computer_sunk_count
    computer_row, computer_column = computer_guess(PLAYERS_BOARD)
    hit_ship = None
    for ship, details in SHIPS.items():
        if PLAYERS_BOARD[computer_row][computer_column] == details["char"]:
            hit_ship = ship
            break
    if hit_ship:
        PLAYERS_BOARD[computer_row][computer_column] = "X"
        print_board(PLAYERS_BOARD)
        print(f"Computer hit your {hit_ship}!\n")
    else:
        PLAYERS_BOARD[computer_row][computer_column] = "-"
        print_board(PLAYERS_BOARD)
        print("Computer missed!\n")




def main():
    """
    Run all game functions.
    """
    place_players_ships(PLAYERS_BOARD)
    create_computer_ships(HIDDEN_BOARD)
    while True:
        players_turn()
        if player_sunk_count == len(SHIPS):
            print(f"Congratulations {name}, you won!")
            break

        computers_turn()
        if computer_sunk_count == len(SHIPS):
            print(f"Sorry {name}, the computer one!")
            break

    restart = input("Do you want to play again? (y/n): ").upper()
    if restart == "Y":
        reset_game()
        main()


print("Welcome to Battleships!")
name = input("What is your name: ")
while not name.isalpha():
    name = input("Enter your name (letter only): ")
main()
