from scramblies import scramble


def test_simple_word():
    s1 = 'rkqodlw'
    s2 = 'world'
    assert scramble(s1, s2)


def test_faslse_result():
    s1 = 'katas'
    s2 = 'steak'
    assert not scramble(s1, s2)


def test_more_complicated():
    s1 = 'scriptjava'
    s2 = 'javascript'
    assert scramble(s1, s2)


def test_real_complicated_stuff():
    s1 = 'scriptingjava'
    s2 = 'javascript'
    assert scramble(s1, s2)


def test_with_emojis():
    s1 = '🍰 is sooo tasty'
    s2 = '🍰'
    assert scramble(s1, s2)


def test_with_symbols():
    s1 = '%$·&$%(/$%(&)) pvj28ru38rpoi3ojfv h89t'
    s2 = 'pv89t'
    assert scramble(s1, s2)


def test_repeated_letters():
    s1 = 'aka'
    s2 = 'akka'
    assert not scramble(s1, s2)
