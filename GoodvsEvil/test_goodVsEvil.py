from goodVsEvil import goodVsEvil


def test_good_triunphs():
    good = '0 0 0 0 0 10'
    evil = '0 1 1 1 1 0 0'
    result = "Battle Result: Good triumphs over Evil"
    assert goodVsEvil(good, evil) == result


def test_evil_triunphs():
    good = '1 1 1 1 1 1'
    evil = '1 1 1 1 1 1 1'
    result = "Battle Result: Evil eradicates all trace of Good"
    assert goodVsEvil(good, evil) == result


def test_due():
    good = '1 0 0 0 0 0'
    evil = '1 0 0 0 0 0 0'
    result = "Battle Result: No victor on this battle field"
    assert goodVsEvil(good, evil) == result
