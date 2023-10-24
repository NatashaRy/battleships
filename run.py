"""
Legend:
PLAYERS_BOARD - Where the computer guesses.
Ships are marked with the first character of the ships name,
hit is marked with 'X' and miss with '-'.

GUESS_BOARD - Where the player guesses.
Hits are marked with the first character of the ship's name,
misses are marked with 'X'.
"""

import random
import re
import os
import time

HIDDEN_BOARD = [["_"] * 8 for _ in range(8)]
GUESS_BOARD = [["_"] * 8 for _ in range(8)]
PLAYERS_BOARD = [["_"] * 8 for _ in range(8)]
PLAYER_SUNK_COUNT = 0
COMPUTER_SUNK_COUNT = 0


def reset_game():
    """
    Resets the game and let the game boards be modified.
    """
    global PLAYER_SUNK_COUNT, COMPUTER_SUNK_COUNT
    HIDDEN_BOARD[:] = [["_"] * 8 for _ in range(8)]
    GUESS_BOARD[:] = [["_"] * 8 for _ in range(8)]
    PLAYERS_BOARD[:] = [["_"] * 8 for _ in range(8)]
    PLAYER_SUNK_COUNT = 0
    COMPUTER_SUNK_COUNT = 0
    for ship, details in SHIPS.items():
        details["sunk"] = False
    for ship in hits_computer:
        hits_computer[ship] = 0
    for ship in hits_player:
        hits_player[ship] = 0


def print_board(board):
    """
    Printing the game boards.
    A-H has headlines for columns and 1-8 marking the row numbers.
    """
    print("  A B C D E F G H")
    row_num = 1
    for row in board:
        print(f"{row_num}|{'|'.join(row)}|")
        row_num += 1


SHIPS = {
    "Battleship": {
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
    Create computer's ships on board randomly,
    placement marked with the ship's character.
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
                    [board[ship_row][ship_column + i] == "_"
                     for i in range(ship_size)]
                ):
                    for i in range(ship_size):
                        board[ship_row][ship_column + i] = ship_char
                    placed = True
            else:
                if all(
                    [board[ship_row + i][ship_column] == "_"
                     for i in range(ship_size)]
                ):
                    for i in range(ship_size):
                        board[ship_row + i][ship_column] = ship_char
                    placed = True


def place_players_ships(board):
    """
    Let players place their ships on board,
    by choosing starting position and orientation.
    Limit players to only enter specific format for guesses (e.g., '1A', '2B').
    Placement marked with the ship's character.
    """
    for ship, details in SHIPS.items():
        ship_char = details["char"]
        ship_size = details["size"]

        placed = False
        while not placed:
            print_board(board)
            print(f"\nPlacing a '{ship}' of size {ship_size} on the board.")

            while True:
                position = input(
                    f"Please enter starting position for {ship} (e.g., A1): "
                ).upper()
                if (
                    len(position) < 2
                    or position[0] not in "ABCDEFGH"
                    or not position[1:].isdigit()
                ):
                    print("Invalid position. Please use the format 'A1'")
                else:
                    break

            column = ord(position[0]) - ord("A")
            row = int(position[1:]) - 1

            while True:
                orientation = input(
                    "Enter orientation (H for horizontal, V for vertical): "
                ).upper()

                if orientation not in ["H", "V"]:
                    print("Invalid orientation. Choose 'H' or 'V'.")
                else:
                    break

            if (orientation == "H" and column + ship_size > 8) or (
                orientation == "V" and row + ship_size > 8
            ):
                print("\nShip placement out of bounds, try again.\n")
                continue

            if orientation == "H":
                if all(
                    board[row][col] == "_"
                    for col in range(column, column + ship_size)
                ):
                    for col in range(column, column + ship_size):
                        board[row][col] = ship_char
                    placed = True
                else:
                    print("Another ship is already in that position.")
            else:
                if all(board[r][column] == "_"
                   for r in range(row, row + ship_size)):
                    for r in range(row, row + ship_size):
                        board[r][column] = ship_char
                    placed = True
                else:
                    print("Another ship is already in that position.")

            if placed:
                print(f"{ship} placed on the board.\n")
    print_board(PLAYERS_BOARD)
    print("All ships have been successfully placed!\n")
    time.sleep(1)
    os.system("cls||clear")


def players_guess():
    """
    Convert letters to numbers, get location of ships.
    Limit players to only enter specific formats for guesses.
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

    pattern = re.compile(r"^[A-Ha-h][1-8]$")

    guess = input("Please enter your guess ('A1'): ").upper().replace("_", "")
    while not pattern.match(guess):
        guess = (
            input("Invalid input. Please enter your guess (e.g., '1A'): ")
            .upper()
            .replace("_", "")
        )

    column = guess[0]
    row = guess[1]

    return int(row) - 1, letters_to_numbers[column]


COMPUTER_LAST_HIT = None
computer_next_guess = ["up", "down", "left", "right"]


def computer_guess(board):
    """
    Let the computer randomly guess the placement of the player's ships.
    Checks if the cell has been guessed or missed before.
    If the last move was a hit, the next move will be in the same area.
    """
    global COMPUTER_LAST_HIT, computer_next_guess

    if COMPUTER_LAST_HIT:
        row, column = COMPUTER_LAST_HIT
        while computer_next_guess:
            direction = random.choice(computer_next_guess)
            computer_next_guess.remove(direction)
            if direction == "up" and row > 0 and board[row - 1][column] == "_":
                return row - 1, column
            elif direction == "down"
            and row < 7 and board[row + 1][column] == "_":
                return row + 1, column
            elif direction == "left"
            and column > 0 and board[row][column - 1] == "_":
                return row, column - 1
            elif direction == "right"
            and column < 7 and board[row][column + 1] == "_":
                return row, column + 1

        COMPUTER_LAST_HIT = None
        computer_next_guess = ["up", "down", "left", "right"]

    column, row = random.randint(0, 7), random.randint(0, 7)
    while board[row][column] == "×" or board[row][column] == "":
        row, column = random.randint(0, 7), random.randint(0, 7)
    return row, column


hits_player = {
    "Battleship": 0,
    "Submarine": 0,
    "Patrol boat": 0,
}


def players_turn():
    """
    Players game logic.
    Check if the player guess has been guessed before.
    Check if any ship is hit/sunk or if the player misses.
    """
    global PLAYER_SUNK_COUNT
    print_board(GUESS_BOARD)

    ship_chars = [details["char"] for details in SHIPS.values()]

    while True:
        row, column = players_guess()
        if GUESS_BOARD[row][column] in ["×"] + ship_chars:
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
                hits_player[hit_ship] += 1

                if (
                    hits_player[hit_ship] == SHIPS[hit_ship]["size"]
                    and not SHIPS[hit_ship]["sunk"]
                ):
                    SHIPS[hit_ship]["sunk"] = True
                    PLAYER_SUNK_COUNT += 1
                    print(f"You have sunk the computers {hit_ship}!\n")
            else:
                print("Miss!\n")
                GUESS_BOARD[row][column] = "×"
            break


hits_computer = {
    "Battleship": 0,
    "Submarine": 0,
    "Patrol boat": 0,
}


def computers_turn():
    """
    Computers game logic.
    """
    global COMPUTER_SUNK_COUNT, COMPUTER_LAST_HIT
    computer_row, computer_column = computer_guess(PLAYERS_BOARD)
    hit_ship = None
    for ship, details in SHIPS.items():
        if PLAYERS_BOARD[computer_row][computer_column] == details["char"]:
            hit_ship = ship
            break

    if hit_ship:
        PLAYERS_BOARD[computer_row][computer_column] = "×"
        print_board(PLAYERS_BOARD)
        print(f"Computer hit your {hit_ship}!\n")
        hits_computer[hit_ship] += 1

        if hits_computer[hit_ship] == SHIPS[hit_ship]["size"]:
            COMPUTER_SUNK_COUNT += 1
            print(f"The computer has sunk your {hit_ship}!\n")
            COMPUTER_LAST_HIT = None
        else:
            COMPUTER_LAST_HIT = (computer_row, computer_column)
    else:
        PLAYERS_BOARD[computer_row][computer_column] = "⁑"
        print_board(PLAYERS_BOARD)
        print("Computer missed!\n")


def main():
    """
    Run all game functions.
    """
    create_computer_ships(HIDDEN_BOARD)
    place_players_ships(PLAYERS_BOARD)
    while True:
        time.sleep(1)
        players_turn()
        if PLAYER_SUNK_COUNT == 3:
            print(f"Congratulations {name}!")
            print("""
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗██╗       ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║██║    ██╗╚██╗
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║██║    ╚═╝ ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║╚═╝    ██╗ ██║
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║██╗    ╚═╝██╔╝
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝       ╚═╝
            """)
            break
        time.sleep(1)

        computers_turn()
        if COMPUTER_SUNK_COUNT == 3:
            print(f"Sorry {name}, the computer won!")
            print("""
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗████████╗██╗        ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝╚══██╔══╝██║    ██╗██╔╝
 ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗   ██║   ██║    ╚═╝██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║   ██║   ╚═╝    ██╗██║
   ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║   ██║   ██╗    ╚═╝╚██╗
   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝        ╚═╝
            """)
            break
    time.sleep(1)
    restart = input("Do you want to play again? (y for yes): ").upper()
    if restart == "Y":
        reset_game()
        main()
    else:
        print(f"Thanks for playing {name}, goodbye!")
        exit()


print("""
       ██╗     ███████╗████████╗███████╗    ██████╗ ██╗      █████╗ ██╗   ██╗
       ██║     ██╔════╝╚══██╔══╝██╔════╝    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝
       ██║     █████╗     ██║   ███████╗    ██████╔╝██║     ███████║ ╚████╔╝
       ██║     ██╔══╝     ██║   ╚════██║    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝
       ███████╗███████╗   ██║   ███████║    ██║     ███████╗██║  ██║   ██║
       ╚══════╝╚══════╝   ╚═╝   ╚══════╝    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝
    """)

print("""
██████╗  █████╗ ████████╗████████╗██╗     ███████╗███████╗██╗  ██╗██╗██████╗ ███████╗
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝██╔════╝██║  ██║██║██╔══██╗██╔════╝
██████╔╝███████║   ██║      ██║   ██║     █████╗  ███████╗███████║██║██████╔╝███████╗
██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  ╚════██║██╔══██║██║██╔═══╝ ╚════██║
██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗███████║██║  ██║██║██║     ███████║
╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚══════╝
""")
name = input("What is your name: ")
while not name.isalpha():
    name = input("Enter your name (letter only): ")
os.system("cls||clear")
main()
