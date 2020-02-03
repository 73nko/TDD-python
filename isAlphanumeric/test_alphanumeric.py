from alphanumeric import alphanumeric


def test_alphanumeric_is_empty():
    word = ""
    result = False
    assert alphanumeric(word) == result


def test_alphanumeric_only_spaces():
    word = "    "
    result = False
    assert alphanumeric(word) == result


def test_alphanumeric_with_underscores():
    word = "a_W0rd"
    result = False
    assert alphanumeric(word) == result


def test_an_alphanumeric_word():
    word = "PassW0rd"
    result = True
    assert alphanumeric(word) == result
