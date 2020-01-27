def check_rows(is_solved, row):
    if all(elem == 1 for elem in row):
        is_solved = 0 if is_solved == 2 else 1
    if all(elem == 2 for elem in row):
        is_solved = 0 if is_solved == 1 else 2
    if any(elem == 0 for elem in row):
        if is_solved != 1 and is_solved != 2:
            is_solved = -1
    return is_solved


def get_column(matrix, i):
    return [row[i] for row in matrix]


def isSolved(board):
    is_solved = 0
    for i, row in enumerate(board):
        column = get_column(board, i)
        is_solved = check_rows(is_solved, row)
        is_solved = check_rows(is_solved, column)
    diagonal_1 = [board[0][0], board[1][1], board[2][2]]
    diagonal_2 = [board[2][2], board[1][1], board[0][0]]
    is_solved = check_rows(is_solved, diagonal_1)
    is_solved = check_rows(is_solved, diagonal_2)
    return is_solved
