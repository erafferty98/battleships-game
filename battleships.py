import random
import numpy as np

Boardsize = [10, 10]
B = "battleship"
C = "cruiser"
D = "destroyer"
S = "submarine"


def is_sunk(ship):
    if ship[3] == len(ship[4]):  # if number of hit = length of ship then ship is sunk
        return True
    else:
        return False


def ship_type(ship):
    # create ships.
    TypeofShip = {4: B, 3: C, 2: D, 1: S}
    return TypeofShip[(ship[3])]  # return type of ship based on length


def is_open_sea(row, column, fleet):
    open_sea = False
    if not ((0 <= row <= Boardsize[0]) and (0 <= column <= Boardsize[1])):  # check coordinates on the board
        return open_sea
    for ship in fleet:  # check coordinates are not already in the fleet
        x, y, horizontal, length = ship[0:4]
        for i in range(length):
            if -1 <= row - x <= 1 and -1 <= column - y <= 1:  # check surrounding ship spaces with new coordinates
                return open_sea
            elif horizontal:
                y += 1
            else:
                x += 1
    open_sea = True
    return open_sea


def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    okay_to_place_ship = False

    if horizontal and not 0 <= column + length <= Boardsize[1]:  # check if coordinates fit on board
        return okay_to_place_ship
    elif not horizontal and not 0 <= row + length <= Boardsize[1]:
        return okay_to_place_ship

    for i in range(length + 1):
        if horizontal:  # check if horizontal and every coordinate of ship will have legal arrangement
            if not is_open_sea(row, column + i, fleet):
                okay_to_place_ship = False
                return okay_to_place_ship
            else:
                for c in range(Boardsize[0]):
                    for r in range(Boardsize[1] - (length - 1)):
                        if is_open_sea(r, c + length, fleet):
                            okay_to_place_ship = True
        else:  # check if vertical coordinates of ship will have legal arrangement
            if not is_open_sea(row + i, column, fleet):
                okay_to_place_ship = False
                return okay_to_place_ship
            else:
                for r in range(Boardsize[1]):
                    for c in range(Boardsize[0] - (length - 1)):
                        if is_open_sea(r + length, c, fleet):
                            okay_to_place_ship = True

    return okay_to_place_ship  # will return true once all coordinates checked and legal


def place_ship_at(row, column, horizontal, length, fleet):
    hits = set()
    fleet.append((row, column, horizontal, length, hits))
    return fleet  # return new fleet with addition of new ship


def randomly_place_all_ships():
    fleet = []
    size = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]  # ships will be placed in order of size

    for length in size:  # iterate over list of ship sizes
        x = random.randint(0, Boardsize[0] - 1)  # random number between 0-9
        y = random.randint(0, Boardsize[1] - 1)  # random number between 0-9
        horizontal = [True, False]
        random.shuffle(horizontal)
        horizontal = horizontal[0]  # random choice of horizontal or not
        while not ok_to_place_ship_at(x, y, horizontal, length,
                                      fleet):  # if None returned generate new random ship info otherwise place ships
            x = random.randint(0, Boardsize[0] - 1)
            y = random.randint(0, Boardsize[1] - 1)
            horizontal = [True, False]
            random.shuffle(horizontal)
            horizontal = horizontal[0]
            ok_to_place_ship_at(x, y, horizontal, length, fleet)
        else:
            place_ship_at(x, y, horizontal, length, fleet)
    return fleet


def check_if_hits(row, column, fleet):
    for ship in fleet:
        x, y, horizontal, length = ship[0:4]
        for i in range(length):
            if (row, column) == (x, y):  # check coordinates in fleet or ship exists with those coordinates
                return True
            elif horizontal:
                y += 1
            elif not horizontal:
                x += 1
    return False


def hit(row, column, fleet):
    fleetindex = 0

    for ship in fleet:
        x, y, horizontal, length = ship[0:4]
        for i in range(length):
            if (row, column) == (x, y):
                ship[4].add((x, y))  # add hit coordinates to set in fleet
                return fleet, fleet[fleetindex]
            if horizontal:
                y += 1
            else:
                x += 1
        fleetindex += 1


def are_unsunk_ships_left(fleet):
    for ship in fleet:
        if len(ship[4]) != ship[3]:  # number of coordinates hit is not equal to length of ship
            return True
    return False


def print_board(board):
    print("\n  " + " ".join(str(x) for x in range(0, Boardsize[0])))  # print board with good spacing and numbering
    for r in range(Boardsize[1]):
        print(str(r) + " " + " ".join(str(c) for c in board[r]))
    print()


def update_board_display(ship, board) -> object:
    for (row, column) in ship[4]:
        if ship[3] == 4:  # if length of ship = 4 ship is battleship board = B
            board[row, column] = B[0].upper()
        elif ship[3] == 3:  # if length of ship = 3 ship is cruiser board = C
            board[row, column] = C[0].upper()
        elif ship[3] == 2:  # if length of ship = 2 ship is destroyer board = D
            board[row, column] = D[0].upper()
        elif ship[3] == 1:  # if length of ship = 1 ship is destroyer board = S
            board[row, column] = S[0].upper()
    return board


def playAgain():
    newGame = input("\nWould you like to play again (y/n)?").lower()
    if newGame[0] == "y":
        main()
    else:
        exit()


def main():
    game_over = False
    shots = 0
    current_fleet = randomly_place_all_ships()
    board_display = np.array([["O"] * Boardsize[1] for x in range(Boardsize[0])])  # display board for player

    print("""Are you ready to play battleships?
    \nRules: There are 10 ships in the ocean  of differing lengths which may be vertical or horizontal; a battleship(4), two cruisers(3),
    three destroyers(2), and four submarines(1).
    \nYour mission is to destroy these randomly placed ships by guessing the coordinates in the format: row column""")

    while not game_over:

        while True:
            print_board(board_display)
            while True:
                user_input = input("Type q to exit or enter row and column to shoot (separated by space): ")
                try:
                    if user_input == "q":
                        exit()
                    else:
                        user_input = user_input.split()
                        current_row = (int(user_input[0]))
                        current_column = (int(user_input[1]))
                except ValueError:
                    print("Sorry, I didn't understand that.")
                    # better try again... Return to the start of the loop
                    continue
                if not ((0 <= current_column < Boardsize[1]) and (0 <= current_row < Boardsize[0])):
                    print("Sorry, you're not in the ocean! try again")
                else:
                    break
            if board_display[current_row, current_column] != 'O':
                print("\nYou guessed that already! That's a miss!")
                shots += 1
            else:
                shots += 1
                break

        if check_if_hits(current_row, current_column, current_fleet):
            print("\nYou have a hit!")
            board_display[current_row, current_column] = 'H'  # update board to represent hit
            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
            if is_sunk(ship_hit):
                typeOfShip = ship_type(ship_hit)
                print("\nYou sank a " + typeOfShip + "!")
                board_display = update_board_display(ship_hit,
                                                     board_display)  # if ship sunk update board to indicate type
        else:
            board_display[current_row, current_column] = 'X'  # update board to indicate miss
            print("\nYou missed!")

        if not are_unsunk_ships_left(current_fleet): game_over = True

    print("\nYou sunk all the ships! \nGame over! You required", shots, "shots.")

    playAgain()  # check if user wants to play again


if __name__ == '__main__':
    main()
