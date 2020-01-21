from sort_the_odd import sort_array


def test_empty_array():
    array = []
    result = []
    assert sort_array(array) == result


def test_sort_odds():
    array = [5, 3, 1]
    result = [1, 3, 5]
    assert sort_array(array) == result


def test_sort_odds_and_leave_pairs():
    array = [5, 3, 2, 8, 1, 4]
    result = [1, 3, 2, 8, 5, 4]
    assert sort_array(array) == result
