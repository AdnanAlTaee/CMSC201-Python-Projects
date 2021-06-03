"""
File:    board.py
Author:  Adnan Al Taee
Date:    04/30/2021
Section: 13
E-mail:  aaltaee1@umbc.edu
Description: This program has a Board class that will be used in the Battleship game
"""
TOTAL_BOARD_LENGTH = 11

SHIPS = {"Carrier": ["CA", 5], "Battleship": ["BA", 4], "Cruiser": ["CR", 3],\
         "Submarine": ["SU", 3], "Destroyer": ["DE", 2]}


class Board:

    def __init__(self, size):

        self.size = size
        self.active_board = []
        self.opp_board = []

    def create_initial_board(self):
        """
        This function creates the initial boards filled with blanks
        :return: a 2d list of strings
        """

        board_list = []

        for i in range(TOTAL_BOARD_LENGTH):

            board_row = []

            for j in range(1):

                if i == 0:

                    board_row.append(" ")

                    for k in range(TOTAL_BOARD_LENGTH - 1):
                        board_row.append(str(k))

                else:

                    board_row.append(str(i - 1))

                    for k in range(TOTAL_BOARD_LENGTH - 1):
                        board_row.append("  ")

            board_list.append(board_row)

        self.active_board = board_list

        self.opp_board = board_list

        return self.active_board

    def draw_board(self, current_board):
        """
        This function draws a board
        :param current_board: a s2d list representing the board
        :return: none
        """

        for i in range(TOTAL_BOARD_LENGTH):

            if i == 0:

                print("  ".join(current_board[i]))

            else:

                print("|".join(current_board[i]), end="")

                print()
        return

    def place_ship(self, board, ship, starting_pos, down_right):
        """
        This function checks if a ship can be placed in a position on the board and
        places it if it can
        :param board: 2d list of strings
        :param ship: string name of ship
        :param starting_pos: list with two numbers for start position of ship
        :param down_right: string "down" or string "right"
        :return: list with new board and if position valid
        """
        row_pos = starting_pos[0] + 1
        col_pos = starting_pos[1] + 1

        len_row = len(board) + 1
        len_col = len(board[0]) + 1

        valid_pos = False

        if down_right == "right":

            # counts number of empty spaces where ship will be placed
            count = 0

            # check if the ship will go out of bounds
            if col_pos + SHIPS[ship][1] < len_col and col_pos >= 0 and row_pos >= 0:

                for i in range(SHIPS[ship][1]):

                    # checks if space on grid is empty
                    if board[row_pos][col_pos + i] == "  ":
                        count = count + 1

                # if all spaces empty count will equal length
                if count == SHIPS[ship][1]:

                    valid_pos = True

                    for i in range(SHIPS[ship][1]):
                        board[row_pos][col_pos + i] = SHIPS[ship][0]
            else:

                valid_pos = False

        if down_right == "down":

            # counts number of empty spaces where ship will be placed
            count = 0

            # check if the ship will go out of bounds
            if row_pos + SHIPS[ship][1] < len_row and row_pos >= 0 and col_pos >= 0:

                for i in range(SHIPS[ship][1]):

                    # checks if space on grid is empty
                    if board[row_pos + i][col_pos] == "  ":
                        count = count + 1

                # if all spaces empty count will equal length
                if count == SHIPS[ship][1]:

                    valid_pos = True

                    for i in range(SHIPS[ship][1]):
                        board[row_pos + i][col_pos] = SHIPS[ship][0]
            else:

                valid_pos = False

        # hold the current board and whether the shot is valid
        output_list = [board, valid_pos]

        return output_list

    def register_shot(self, x, y, board, opp_board):
        """
        This function checks if the fired shot is a hit or miss and if the position has
        already been hit or missed

        :param x: integer row position
        :param y: integer column position
        :param board: 2d list of string
        :param opp_board: 2d list of string
        :return: string where the shot landed
        """

        ship_hit = "Miss"
        x = x + 1
        y = y + 1

        if x < 0 or x >= len(board) or y < 0 or y >= len(board):

            return "out of bounds"

        else:

            if board[x][y] == "CA":

                ship_hit = "Carrier"

            if board[x][y] == "BA":

                ship_hit = "Battleship"

            if board[x][y] == "CR":

                ship_hit = "Cruiser"

            if board[x][y] == "SU":

                ship_hit = "Submarine"

            if board[x][y] == "DE":

                ship_hit = "Destroyer"

            if opp_board[x][y] == "HH":

                return "already hit"

            if opp_board[x][y] == "MM":

                return "already missed"

        return ship_hit

