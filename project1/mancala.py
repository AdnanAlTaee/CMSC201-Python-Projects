"""
File:    mancala.py
Author:  Adnan Al Taee
Date:    04/09/2021
Section: 13
E-mail:  aaltaee1@umbc.edu
Description: This program is a simple game of mancala consisting of two real world players
"""

BLOCK_WIDTH = 6
BLOCK_HEIGHT = 5
BLOCK_SEP = "*"
SPACE = ' '

NUM_PLAYERS = 2

NUM_CUPS = 6

# the position of the first cup on the board
FIRST_CUP = 1


# the position of the last cup on the board
LAST_CUP = 13

# value for who's turn it is
PLAYER_ONE = 0

# value for when it's player twos turn
PLAYER_TWO = 1

# value for when game ends in a draw
DRAW = 3

# the value that ensures that stones loop back around when being moved
RESET_VALUE = 14

# mancala positions on the board
MANCALA_POSITIONS = [0, 7]

# first position to check cups in top row
FIRST_CUP_TOP_ROW = 0

# last position to check cups in top row
LAST_CUP_TOP_ROW = 6

# first position to check cups in bottom row
FIRST_CUP_BOT_ROW = 7

# last position to check cups in bottom row
LAST_CUP_BOT_ROW = 13

# initial positions for all stones on the board
START_POSITIONS = ["0", "4", "4", "4", "4", "4", "4", "0", "4", "4", "4", "4", "4", "4"]

# value for 6 empty cups in a row
EMPTY_ROW = 6


def draw_board(top_cups, bottom_cups, mancala_a, mancala_b):
    """
    draw_board is the function that you should call in order to draw the board.
        top_cups and bottom_cups are 2d lists of strings.  Each string should be length BLOCK_WIDTH and each list should be of length BLOCK_HEIGHT.
        mancala_a and mancala_b should be 2d lists of strings.  Each string should be BLOCK_WIDTH in length, and each list should be 2 * BLOCK_HEIGHT + 1

    :param top_cups: This should be a list of strings that represents cups 1 to 6 (Each list should be at least BLOCK_HEIGHT in length, since each string in\
 the list is a line.)
    :param bottom_cups: This should be a list of strings that represents cups 8 to 13 (Each list should be at least BLOCK_HEIGHT in length, since each strin\
g in the list is a line.)
    :param mancala_a: This should be a list of 2 * BLOCK_HEIGHT + 1 in length which represents the mancala at position 7.
    :param mancala_b: This should be a list of 2 * BLOCK_HEIGHT + 1 in length which represents the mancala at position 0.
    """
    board = [[SPACE for _ in range((BLOCK_WIDTH + 1) * (len(top_cups) + 2) + 1)] for _ in range(BLOCK_HEIGHT * 2 + 3)]
    for p in range(len(board)):
        board[p][0] = BLOCK_SEP
        board[p][len(board[0]) - 1] = BLOCK_SEP

    for q in range(len(board[0])):
        board[0][q] = BLOCK_SEP
        board[len(board) - 1][q] = BLOCK_SEP

    # draw midline
    for p in range(BLOCK_WIDTH + 1, (BLOCK_WIDTH + 1) * (len(top_cups) + 1) + 1):
        board[BLOCK_HEIGHT + 1][p] = BLOCK_SEP

    for i in range(len(top_cups)):
        for p in range(len(board)):
            board[p][(1 + i) * (1 + BLOCK_WIDTH)] = BLOCK_SEP

    for p in range(len(board)):
        board[p][1 + BLOCK_WIDTH] = BLOCK_SEP
        board[p][len(board[0]) - BLOCK_WIDTH - 2] = BLOCK_SEP

    for i in range(len(top_cups)):
        draw_block(board, i, 0, top_cups[i])
        draw_block(board, i, 1, bottom_cups[i])

    draw_mancala(0, mancala_a, board)
    draw_mancala(1, mancala_b, board)

    print('\n'.join([''.join(board[i]) for i in range(len(board))]))


def draw_mancala(fore_or_aft, mancala_data, the_board):
    """
        Draw_mancala is a helper function for the draw_board function.
    :param fore_or_aft: front or back (0, or 1)
    :param mancala_data: a list of strings of length 2 * BLOCK_HEIGHT + 1 each string of length BLOCK_WIDTH
    :param the_board: a 2d-list of characters which we are creating to print the board.
    """
    if fore_or_aft == 0:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            # data = mancala_data[i][0: BLOCK_WIDTH]
            for j in range(len(mancala_data[0])):
                the_board[1 + i][1 + j] = data[j]
    else:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            # data = mancala_data[i][0: BLOCK_WIDTH]
            for j in range(len(mancala_data[0])):
                the_board[1 + i][len(the_board[0]) - BLOCK_WIDTH - 1 + j] = data[j]


def draw_block(the_board, pos_x, pos_y, block_data):
    """
        Draw block is a helper function for the draw_board function.
    :param the_board: the board is the 2d grid of characters we're filling in
    :param pos_x: which cup it is
    :param pos_y: upper or lower
    :param block_data: the list of strings to put into the block.
    """
    for i in range(BLOCK_HEIGHT):
        data = block_data[i][0:BLOCK_WIDTH].rjust(BLOCK_WIDTH)
        for j in range(BLOCK_WIDTH):
            the_board[1 + pos_y * (BLOCK_HEIGHT + 1) + i][1 + (pos_x + 1) * (BLOCK_WIDTH + 1) + j] = data[j]


def get_player():
    """
    This function gets the names of player 1 and player 2
    :return: a list of the two names
    """

    player_list = []

    # adds player names to a list
    for i in range(NUM_PLAYERS):
        name = input("Player {} please enter your name: ".format(i + 1))

        player_list.append(name)

    return player_list


def take_turn(players, who, cups):
    """
    This function displays the board and asks for new moves
    :param players: list of strings with player names
    :param who: integer who's turn it is
    :param cups: list of cups with number of stones
    :return: returns a list with new stone locations and whether last stone was on a mancala
    """

    # calls board info function to display board
    board_info(players, cups)

    # sets current player to player one or player two
    if who == PLAYER_ONE:

        current_player = players[PLAYER_ONE]

    else:

        current_player = players[PLAYER_TWO]

    player_turn = input("{}, What cup do you want to move? ".format(current_player))

    # calls check_valid() to check if the entered move is valid
    valid_turn = check_valid(player_turn, cups)

    # keeps looping to check valid turns until one is valid
    while not valid_turn:

        player_turn = input("{}, invalid cup :(, please pick another: ".format(current_player))

        valid_turn = check_valid(player_turn, cups)

    # casts to int to prepare for make_move() function
    int_player_turn = int(player_turn)

    # calls make_move() to actually move stones
    turn_end_list = make_move(int_player_turn, cups)

    return turn_end_list


def make_move(start_cup, cup_list):
    """
    This function moves the stones around the board for a turn and checks if the stones stop on a mancala
    :param start_cup: integer value of cup chosen
    :param cup_list: list of current stone positions on board
    :return: a list with the new board positions and a boolean for the stones stopping on a mancala
    """

    end_on_mancala = False

    # get number of stones in cup and cast to integer
    stones_in_cup = int(cup_list[start_cup])

    # add one so it starts on the next cup
    current_position = start_cup + 1

    cup_list[start_cup] = "0"

    for i in range(stones_in_cup):

        # checks if the position is more than 13
        if current_position > int(LAST_CUP):

            # resets number so it continues to next correct cup
            current_position = current_position - int(RESET_VALUE)

        # adds a stone to cup and then casts it back to string
        cup_list[current_position] = str(int(cup_list[current_position]) + 1)

        current_position = current_position + 1

    # subtracts one to get the position where the stones stopped
    last_position = current_position - 1

    if last_position in MANCALA_POSITIONS:

        end_on_mancala = True

    move_made_list = [end_on_mancala, cup_list]

    return move_made_list


def check_valid(cup_number, num_stones):
    """
    This function checks if the chosen cup is valid
    :param cup_number: integer of which position is chosen
    :param num_stones: list of current number of stones in each cup
    :return: True if the number is valid False if not
    """

    # integer casting of cup_number argument
    cup_num = int(cup_number)

    if cup_num < FIRST_CUP_TOP_ROW or cup_num > LAST_CUP_BOT_ROW or cup_num == MANCALA_POSITIONS[0] \
            or cup_num == MANCALA_POSITIONS[1]:

        is_valid = False

    elif num_stones[cup_num] == "0":

        is_valid = False

    else:

        is_valid = True

    return is_valid


def run_game():
    """
    This function runs the game
    :return: does not return anything
    """

    # calls get_player() to get names
    player_list = get_player()

    player_turn = PLAYER_ONE

    current_positions = START_POSITIONS

    game_over_check = game_over(current_positions)

    # game_over_check[0] will be either True or False
    while not game_over_check[0]:

        # calls take_turn() to play that players turn
        play_turn = take_turn(player_list, player_turn, current_positions)

        # sets it to the list of stone positions
        new_positions = play_turn[1]

        game_over_check = game_over(new_positions)

        if game_over_check[0]:

            if game_over_check[1] == PLAYER_ONE:

                print("{} is the winner!".format(player_list[PLAYER_ONE]))

            elif game_over_check[1] == PLAYER_TWO:

                print("{} is the winner!".format(player_list[PLAYER_TWO]))

            else:

                print("The game has ended in a draw!")

        # this is for the last stone landing on a mancala
        elif play_turn[0]:

            print("Your last stone landed in a mancala.")
            print("That means you get an extra turn!")

        else:

            if player_turn == PLAYER_ONE:

                player_turn = PLAYER_TWO

            else:

                player_turn = PLAYER_ONE

        current_positions = new_positions

    return


def game_over(stones_list):
    """
    This function checks if the win condition has been met
    :param stones_list: the list of stone positions on the board
    :return: returns a list that confirms if the win condition has been met and who has won
    """

    win_condition_met = False

    # counts how many cups in top row are empty
    top_row_zeroes = 0

    # counts how many cups in bottom row are empty
    bot_row_zeroes = 0

    # adds to count if cup is empty in top row
    for i in range(FIRST_CUP_TOP_ROW, LAST_CUP_TOP_ROW):

        if stones_list[i + 1] == "0":

            top_row_zeroes = top_row_zeroes + 1

    # adds to count if cup is empty in bottom row
    for i in range(FIRST_CUP_BOT_ROW, LAST_CUP_BOT_ROW):

        if stones_list[i + 1] == "0":

            bot_row_zeroes = bot_row_zeroes + 1

    if top_row_zeroes == EMPTY_ROW or bot_row_zeroes == EMPTY_ROW:

        win_condition_met = True

    # if the game is not over yet
    winner = -1

    if win_condition_met:

        # if player 1 has more stones
        if int(stones_list[MANCALA_POSITIONS[1]]) > int(stones_list[MANCALA_POSITIONS[0]]):

            winner = 0

        # if player 2 has more stones
        elif int(stones_list[MANCALA_POSITIONS[0]]) > int(stones_list[MANCALA_POSITIONS[1]]):

            winner = 1

        else:

            winner = -1

    end_game = [win_condition_met, winner]

    return end_game


def board_info(player_names, stones_list):
    """
    This function places the players names and number of stones in each cup to send to draw_board
    :param player_names: A list with the two names
    :param stones_list:  A list with the number of stones in each cup
    :return: does not return anything
    """

    top_cup_loop = []

    cup_num = FIRST_CUP

    # organizes and adds each top row cup area
    for i in range(NUM_CUPS):

        top_cup_row = []

        for j in range(1):
            top_cup_row.append("Cup   ")
            top_cup_row.append(str(cup_num))
            top_cup_row.append("Stones")
            top_cup_row.append(stones_list[i + 1])
            top_cup_row.append("      ")

        cup_num = cup_num + 1
        top_cup_loop.append(top_cup_row)

    bot_cup_loop = []

    cup_num = LAST_CUP

    # organizes and adds each bottom row cup area
    for i in range(NUM_CUPS):

        bot_cup_row = []

        for j in range(1):
            bot_cup_row.append("Cup   ")
            bot_cup_row.append(str(cup_num))
            bot_cup_row.append("Stones")
            bot_cup_row.append(stones_list[cup_num])
            bot_cup_row.append("      ")

        cup_num = cup_num - 1
        bot_cup_loop.append(bot_cup_row)

    # right side mancala
    mancala_list_b = []

    mancala_list_b.append("      ")
    mancala_list_b.append("      ")
    mancala_list_b.append("      ")
    mancala_list_b.append(player_names[0])
    mancala_list_b.append("      ")
    mancala_list_b.append("      ")
    mancala_list_b.append("      ")
    mancala_list_b.append("Stones")
    mancala_list_b.append(stones_list[7])
    mancala_list_b.append("      ")
    mancala_list_b.append("      ")

    # left side mancala
    mancala_list_a = []

    mancala_list_a.append("      ")
    mancala_list_a.append("      ")
    mancala_list_a.append("      ")
    mancala_list_a.append(player_names[1])
    mancala_list_a.append("      ")
    mancala_list_a.append("      ")
    mancala_list_a.append("      ")
    mancala_list_a.append("Stones")
    mancala_list_a.append(stones_list[0])
    mancala_list_a.append("      ")
    mancala_list_a.append("      ")

    # calls draw board to actually draw the board(thanks Eric)
    draw_board(top_cup_loop, bot_cup_loop, mancala_list_a, mancala_list_b)

    return


if __name__ == "__main__":

    run_game()

