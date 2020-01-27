from ticTacToeSolver import isSolved

NOT_RESOLVED = -1
WON_1 = 1
WON_2 = 2
DRAW = 0


def test_is_not_solved():
    board = [[0, 0, 1],
             [0, 1, 2],
             [2, 1, 0]]
    assert isSolved(board) == NOT_RESOLVED


def test_is_solved_row_won1():
    board = [[1, 2, 1],
             [1, 1, 1],
             [2, 1, 2]]
    assert isSolved(board) == WON_1


def test_is_solved_column_won1():
    board = [[1, 1, 1], [0, 2, 2], [0, 0, 0]]
    assert isSolved(board) == WON_1


def test_is_solved_row_won2():
    board = [[2, 1, 1],
             [1, 1, 2],
             [2, 2, 2]]
    assert isSolved(board) == WON_2


def test_is_solved_column_won2():
    board = [[1, 2, 2],
             [2, 1, 2],
             [1, 1, 2]]
    assert isSolved(board) == WON_2


def test_is_draw_row():
    board = [[1, 1, 1],
             [1, 1, 2],
             [2, 2, 2]]
    assert isSolved(board) == DRAW
