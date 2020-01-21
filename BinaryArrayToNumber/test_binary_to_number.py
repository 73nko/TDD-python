from binary_to_number import binary_array_to_number


def test_binary_to_number_returns_1():
    array = [0, 0, 0, 1]
    expectedResult = 1
    assert binary_array_to_number(array) == expectedResult


def test_binary_to_number_returns_2():
    array = [0, 0, 1, 0]
    expectedResult = 2
    assert binary_array_to_number(array) == expectedResult


def test_binary_to_number_returns_15():
    array = [1, 1, 1, 1]
    expectedResult = 15
    assert binary_array_to_number(array) == expectedResult


def test_binary_to_number_returns_6():
    array = [0, 1, 1, 0]
    expectedResult = 6
    assert binary_array_to_number(array) == expectedResult
