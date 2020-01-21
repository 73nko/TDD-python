from stringToCamelCase import to_camel_case


def test_empty_string():
    word = ''
    result = ''
    assert to_camel_case(word) == result


def test_word_with_dash():
    word = 'The-Stealth-Warrior'
    result = 'TheStealthWarrior'
    assert to_camel_case(word) == result


def test_capitalize_words_but_first():
    word = 'the-stealth-warrior'
    result = 'theStealthWarrior'
    assert to_camel_case(word) == result


def test_words_with_underscore():
    word = 'the_stealth_warrior'
    result = 'theStealthWarrior'
    assert to_camel_case(word) == result
