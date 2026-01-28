board = [
    "   a     b     c",     # index 0
    "      |     |     ",   # index 1
    "1  -  |  -  |  -  ",   # index 2
    " _____|_____|_____",   # index 3
    "      |     |     ",   # index 4
    "2  -  |  -  |  -  ",   # index 5
    " _____|_____|_____",   # index 6
    "      |     |     ",   # index 7
    "3  -  |  -  |  -  ",   # index 8
    "      |     |     "    # index 9
]

# Print the original table
# Note: board is a list, now we are printing each element of the list
for line in board:
    print(line)

# Mapping the table
line_map = {
    1: 2,
    2: 5,
    3: 8
}

col_map = {
    "a": 3,
    "b": 9,
    "c": 15
}

# ------------------------------------------------------------------------------

# Input of the player X
def input_x():
    lx = int(input("Player X, please select a line(1-3): "))
    cx = input("Player X, now select a column(a, b or c): ").lower()

    row_index = line_map[lx]
    col_index = col_map[cx]

    row = board[row_index]
    row = row[:col_index] + "X" + row[col_index+1:]  # before + X + after
    board[row_index] = row

    for line in board:  # New table
        print(line)

# ------------------------------------------------------------------------------

# Input of the player 0
def input_0():
    l0 = int(input("Player 0, please select a line(1-3): "))
    c0 = input("Player 0, now select a column(a, b or c): ").lower()

    row_index = line_map[l0]
    col_index = col_map[c0]

    row = board[row_index]
    row = row[:col_index] + "0" + row[col_index+1:]  # before + 0 + after
    board[row_index] = row

    for rows in board:  # New table
        print(rows)

# ------------------------------------------------------------------------------

def win_x():

    # columns
    for row in [1, 2, 3]:
        if (
            board[line_map[row]][col_map["a"]] == "X" and
            board[line_map[row]][col_map["b"]] == "X" and
            board[line_map[row]][col_map["c"]] == "X"
        ):
            return True

    # lines
    for column in ["a", "b", "c"]:
        if (
            board[line_map[1]][col_map[column]] == "X" and
            board[line_map[2]][col_map[column]] == "X" and
            board[line_map[3]][col_map[column]] == "X"
        ):
            return True

    # main diagonal (a1, b2, c3)
    if (
        board[line_map[1]][col_map["a"]] == "X" and
        board[line_map[2]][col_map["b"]] == "X" and
        board[line_map[3]][col_map["c"]] == "X"
    ):
        return True

# other diagonal (c1, b2, a3)
    if (
        board[line_map[1]][col_map["c"]] == "X" and
        board[line_map[2]][col_map["b"]] == "X" and
        board[line_map[3]][col_map["a"]] == "X"
    ):
        return True


    return False

# ------------------------------------------------------------------------------


def win_0():

    # columns
    for row in [1, 2, 3]:
        if (
            board[line_map[row]][col_map["a"]] == "0" and
            board[line_map[row]][col_map["b"]] == "0" and
            board[line_map[row]][col_map["c"]] == "0"
        ):
            return True

    # lines
    for column in ["a", "b", "c"]:
        if (
            board[line_map[1]][col_map[column]] == "0" and
            board[line_map[2]][col_map[column]] == "0" and
            board[line_map[3]][col_map[column]] == "0"
        ):
            return True

    # main diagonal (a1, b2, c3)
    if (
        board[line_map[1]][col_map["a"]] == "0" and
        board[line_map[2]][col_map["b"]] == "0" and
        board[line_map[3]][col_map["c"]] == "0"
    ):
        return True

# other diagonal (c1, b2, a3)
    if (
        board[line_map[1]][col_map["c"]] == "0" and
        board[line_map[2]][col_map["b"]] == "0" and
        board[line_map[3]][col_map["a"]] == "0"
    ):
        return True


    return False

# ------------------------------------------------------------------------------

# Looping
for i in range(9):
    if i % 2 == 0:
        input_x()

    else:
        input_0()

    # X win conditions
    if win_x():
        print("Player X won !!")
        break
    # 0 win conditions
    if win_0():
        print("Player 0 won !!")
        break
