import random


def init_new_board():
    board = []
    for index in range(0, 9):
        board.append("-")
    return board


def display():
    global board
    print("========BOARD========")
    for index in range(1, 10):
        print(board[index - 1], end=" ")
        if index % 3 == 0:
            print("\n")
    print("=====================")


def player_move():
    global board
    accepted_input = False
    while not accepted_input:
        index = int(input("Player input index: "))
        if board[index] == "-":
            accepted_input = True
            board[index] = "O"
        else:
            print("WRONG INPUT")


def computer_move():
    global board
    index = random.randint(0, 8)
    while board[index] != "-":
        index = random.randint(0, 8)
    board[index] = "X"


def check_result(player):
    global board
    if player == "player":
        mark = "O"
    else:
        mark = "X"
    is_winner = False
    if (board[0] == board[1] == board[2] == mark) \
            or (board[3] == board[4] == board[5] == mark) \
            or (board[6] == board[7] == board[8] == mark) \
            or (board[0] == board[3] == board[6] == mark) \
            or (board[1] == board[4] == board[7] == mark) \
            or (board[2] == board[5] == board[8] == mark) \
            or (board[0] == board[4] == board[8] == mark) \
            or (board[2] == board[4] == board[6] == mark):
        print("{} wins".format(player))
        is_winner = True

    is_board_full = True
    for item in board:
        if item == "-":
            is_board_full = False
            break

    if is_board_full:
        print("BOARD FULL, TIED")

    return is_winner or is_board_full


board = init_new_board()
display()

while True:
    player_move()
    display()
    if check_result("player"):
        break
    computer_move()
    display()
    if check_result("computer"):
        break

