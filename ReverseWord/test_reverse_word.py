from reverse_word import reverse_words


def test_reverse_word_prueba():
    word = "prueba"
    result = "abeurp"
    assert reverse_words(word) == result


def test_reverse_word_apple():
    word = "apple"
    result = "elppa"
    assert reverse_words(word) == result


def test_reverse_two_words():
    two_words = "the car"
    result = "eht rac"
    assert reverse_words(two_words) == result


def test_reverse_full_sentence():
    sentence = 'The quick brown fox jumps over the lazy dog.'
    result = 'ehT kciuq nworb xof spmuj revo eht yzal .god'
    assert reverse_words(sentence) == result
