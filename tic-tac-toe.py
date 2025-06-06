#
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
#if game is still going
game_still_going = True

#who won
winer = None

#whose turn is it
current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2] )
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():

    display_board()

    while game_still_going:


        handle_turn(current_player)

        #check if game is ended
        check_if_game_over()

        #swithc to other player
        flip_player()

    #check if game is over
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Draw.")


def handle_turn(player):

    print(player + "'s turn.")
    position= input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid position. Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there, Go again.")

    board[position] = player
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():

    #set up global var
    global winner

    #check row
    row_winner = check_row()
    #check column
    column_winner = check_column()
    #check diagonal
    diagonal_winner = check_diagonal()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return

def check_row():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return
    return

def check_column():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return
    return

def check_diagonal():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()
