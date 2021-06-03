"""
File:    battleship.py
Author:  Adnan Al Taee
Date:    04/30/2021
Section: 13
E-mail:  aaltaee1@umbc.edu
Description: This program allows to players to play a game of Battleship against each other
"""
from board import Board

TOTAL_BOARD_LENGTH = 11

SHIPS = {"Carrier": ["CA", 5], "Battleship": ["BA", 4], "Cruiser": ["CR", 3], \
         "Submarine": ["SU", 3], "Destroyer": ["DE", 2]}

PLAYER_ONE = "p1"

PLAYER_TWO = "p2"


class BattleshipGame:

    def __init__(self, size=10, ):

        self.size = size
        self.player_1 = Board(10)
        self.player_2 = Board(10)
        self.player_one_board = []
        self.player_two_board = []
        self.p_one_opp_board = []
        self.p_two_opp_board = []

    def run_game(self):

        # creates blank boards
        player_one_board = self.player_1.create_initial_board()
        player_two_board = self.player_2.create_initial_board()

        # creates blank opponent boards
        self.p_one_opp_board = list(self.player_1.create_initial_board())
        self.p_two_opp_board = list(self.player_2.create_initial_board())

        print("Player 1, prepare to place your fleet")

        # place ships for p1
        self.player_one_board = BattleshipGame().place_ships(player_one_board)

        print("Player 2, prepare to place your fleet")

        # place ships for p2
        self.player_two_board = BattleshipGame().place_ships(player_two_board)

        # counts the ships ships hit for p1 and p2
        p_1_ships = {"Carrier": 0, "Battleship": 0, "Cruiser": 0, \
                     "Submarine": 0, "Destroyer": 0}

        p_2_ships = {"Carrier": 0, "Battleship": 0, "Cruiser": 0, \
                     "Submarine": 0, "Destroyer": 0}

        # win condition check
        game_over = False
        current_turn = PLAYER_ONE
        while not game_over:

            valid_shot = False
            if current_turn == PLAYER_ONE:

                # loops if the shot is invalid and game is not over
                while not valid_shot and not game_over:

                    # display boards for p1 and opponents hits and misses
                    BattleshipGame().display_boards(PLAYER_ONE, self.player_one_board, self.p_one_opp_board)

                    fire_pos_str = input("Enter x y coordinates to fire: ")

                    fire_pos = fire_pos_str.split(" ")

                    # casts str to int
                    fire_pos[0] = int(fire_pos[0])
                    fire_pos[1] = int(fire_pos[1])

                    # calls register shot which checks were the shot will land
                    shot_landed = self.player_1.register_shot(fire_pos[0], fire_pos[1], \
                                                              self.player_two_board, self.p_one_opp_board)

                    if shot_landed == "out of bounds":

                        print("Shot of the grid, give new coordinates.")

                    elif shot_landed == "already hit":

                        print("You have already shot there and hit something.")

                    elif shot_landed == "already missed":

                        print("You have already shot there, and missed.")

                    elif shot_landed == "Miss":

                        valid_shot = True
                        print("This shot was a miss!")
                        current_turn = PLAYER_TWO
                        self.player_two_board[fire_pos[0] + 1][fire_pos[1] + 1] = "MM"
                        self.p_one_opp_board[fire_pos[0] + 1][fire_pos[1] + 1] = "MM"

                    else:

                        valid_shot = True

                        # add 1 to shots hit on a ship
                        p_2_ships[shot_landed] = p_2_ships[shot_landed] + 1

                        # this checks if the ship is sunk or not
                        if p_2_ships[shot_landed] == SHIPS[shot_landed][1]:

                            print("You sunk the {}".format(shot_landed))
                        else:
                            print("You hit the {}".format(shot_landed))

                        current_turn = PLAYER_TWO
                        self.player_two_board[fire_pos[0] + 1][fire_pos[1] + 1] = "HH"
                        self.p_one_opp_board[fire_pos[0] + 1][fire_pos[1] + 1] = "HH"

                        total_hit = 0
                        # sums all the hits
                        for values in p_2_ships:
                            total_hit = total_hit + p_2_ships[values]

                        # 17 hits means that all ships have been sunk
                        if total_hit == 17:
                            winner = PLAYER_ONE
                            game_over = True

            if current_turn == PLAYER_TWO:

                # loops if the shot is invalid and game is not over
                while not valid_shot and not game_over:

                    # display boards for p2 and opponents hits and misses
                    BattleshipGame().display_boards(PLAYER_TWO, self.player_two_board, self.p_two_opp_board)

                    fire_pos_str = input("Enter x y coordinates to fire: ")

                    fire_pos = fire_pos_str.split(" ")

                    # casts str to int
                    fire_pos[0] = int(fire_pos[0])
                    fire_pos[1] = int(fire_pos[1])

                    # calls register shot which checks were the shot will land
                    shot_landed = self.player_1.register_shot(fire_pos[0], fire_pos[1], \
                                                              self.player_one_board, self.p_two_opp_board)

                    if shot_landed == "out of bounds":

                        print("Shot of the grid, give new coordinates.")

                    elif shot_landed == "already hit":

                        print("You have already shot there and hit something.")

                    elif shot_landed == "already missed":

                        print("You have already shot there, and missed.")

                    elif shot_landed == "Miss":

                        valid_shot = True
                        print("This shot was a miss!")
                        current_turn = PLAYER_ONE
                        self.player_one_board[fire_pos[0] + 1][fire_pos[1] + 1] = "MM"
                        self.p_two_opp_board[fire_pos[0] + 1][fire_pos[1] + 1] = "MM"

                    else:

                        valid_shot = True

                        # add 1 to shots hit on a ship
                        p_1_ships[shot_landed] = p_1_ships[shot_landed] + 1

                        # this checks if the ship is sunk or not
                        if p_1_ships[shot_landed] == SHIPS[shot_landed][1]:

                            print("You sunk the {}".format(shot_landed))
                        else:
                            print("You hit the {}".format(shot_landed))

                        current_turn = PLAYER_ONE
                        self.player_one_board[fire_pos[0] + 1][fire_pos[1] + 1] = "HH"
                        self.p_two_opp_board[fire_pos[0] + 1][fire_pos[1] + 1] = "HH"

                        total_hit = 0
                        # sums all the hits
                        for values in p_1_ships:

                            total_hit = total_hit + p_1_ships[values]

                        # 17 hits means that all ships have been sunk
                        if total_hit == 17:

                            winner = PLAYER_TWO
                            game_over = True

        # displays final boards for each player
        BattleshipGame().display_boards(PLAYER_ONE, self.player_one_board, self.player_two_board)

        if winner == "p1":

            print("Player 1 has won.")

        else:

            print("Player 2 has won.")

        return

    def place_ships(self, player_board):
        """
        This function will place all the ships at the start of the game
        :param player_board: a 2d list representing the board
        :return: 2d list with ships placed
        """

        final_board = player_board
        # loops through all  the ships
        for key in SHIPS:

            self.player_1.draw_board(final_board)

            # false if a ship has not been placed because of invalid position
            valid_pos = False

            # will keep going until a ship is placed correctly
            while not valid_pos:

                ship_pos_str = input("Enter x y coordinates to place the {}: ".format(key))
                ship_pos = ship_pos_str.split(" ")

                # change string to int
                ship_pos[0] = int(ship_pos[0])
                ship_pos[1] = int(ship_pos[1])

                r_or_d = input("Enter Right or Down (r or d) ")

                if r_or_d == "r":
                    r_or_d = "right"

                if r_or_d == "d":
                    r_or_d = "down"

                # call Board type method to check if ship can be placed and place ship
                new_board_check = self.player_1.place_ship(final_board, key, ship_pos, r_or_d)

                # new board check[1] holds true for valid position and False for invalid
                if new_board_check[1] == False:

                    print("Invalid position or overlapping ships, try again.")

                else:

                    # assigns new board that is returned from the place_ship method(in the Board class)
                    final_board = new_board_check[0]
                    valid_pos = True

        return final_board

    def display_boards(self, turn, active_board, opp_board):
        """
        This function will display the current players board and the hits and misses of the
        opponents fleet
        :param turn: string p1 or p2 to indicate current turn
        :return: none
        """

        if turn == "p1":

            self.player_1.draw_board(active_board)

            print()

            self.player_1.draw_board(opp_board)

        else:

            self.player_2.draw_board(active_board)

            print()

            self.player_2.draw_board(opp_board)


if __name__ == "__main__":
    BattleshipGame().run_game()
