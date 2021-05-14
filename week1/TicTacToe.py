table = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]


def is_winner_on_row(mat):
    for row in mat:
        if row.count(1) == 3:
            return 1
        elif row.count(0) == 3:
            return 0
    return -1


def is_winner_on_column(mat):
    for i in range(3):
        col = [row[i] for row in mat]
        if col.count(1) == 3:
            return 1
        if col.count(0) == 3:
            return 0
    return -1


def is_winner_on_diagonals(mat):
    diagonal = [mat[i][i] for i in range(3)]
    if diagonal.count(0) == 3:
        return 0
    if diagonal.count(1) == 3:
        return 1
    diagonal = [mat[i][i] for i in range(2, -1, -1)]
    if diagonal.count(0) == 3:
        return 0
    if diagonal.count(1) == 3:
        return 1
    return -1


def check_if_winner(mat):
    if is_winner_on_diagonals(mat) != -1:
        return is_winner_on_diagonals(mat)
    elif is_winner_on_column(mat) != -1:
        return is_winner_on_column(mat)
    elif is_winner_on_row(mat) != -1:
        return is_winner_on_row(mat)
    return -1


def get_player(move):
    return 'X' if move == 1 else 'O'


def print_table(mat):
    for row in mat:
        print('\n-------------------')
        for el in row:
            print('|  {}  '.format(get_player(el) if el != -1 else ' '), end='')
        print('|', end='')
    print('\n-------------------')


def check_position(position, mat):
    try:
        row = int(position[0])
        column = int(position[1])
    except ValueError:
        print('Invalid numbers')
        return -1

    if len(position) > 2 or row > 2 or column > 2:
        print('Invalid position! Try again')
        return -1
    if mat[row][column] != -1:
        print("Position already used! Try again")
        return -1
    return 0


def mark_position(position, mat, move):
    row = int(position[0])
    column = int(position[1])
    mat[row][column] = move


def get_move(move):
    return 0 if move == 1 else 1


def verify_valid_positions_exists(mat):
    for i in mat:
        if i.count(-1):
            return 0
    return -1


def play_game(mat, current_move):
    print_table(mat)
    move = current_move
    position = input("Select a position (row and column): ")
    while check_position(position, mat):
        position = input("Select a position (row and column): ")
    if not (check_position(position, mat)):
        move = get_move(current_move)
        mark_position(position, mat, move)
    if check_if_winner(mat) != -1:
        print("\n\n{} is the winner".format(get_player(check_if_winner(mat))))
        print_table(mat)
    elif verify_valid_positions_exists(mat) == -1:
        print("Draw!")
    else:
        play_game(mat, move)


play_game(table, 0)
