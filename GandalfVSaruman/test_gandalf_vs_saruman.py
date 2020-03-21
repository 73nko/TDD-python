from gandalf_vs_saruman import gandalf_vs_saruman


def test_no_winner():
    gandalf_spells = [2, 3, 4, 5, 6, 2, 2]
    saruman_spells = [3, 4, 3, 2, 7, 5, 1]
    assert gandalf_vs_saruman(gandalf_spells, saruman_spells) == "NO WINNER"


def test_saruman_wins():
    gandalf_spells = [2, 3, 4, 5, 6, 2, 2]
    saruman_spells = [3, 4, 3, 7, 7, 5, 1]
    assert gandalf_vs_saruman(gandalf_spells, saruman_spells) == "SARUMAN WINS"


def test_gandalf_wins():
    gandalf_spells = [2, 3, 4, 5, 6, 2, 2]
    saruman_spells = [3, 4, 3, 2, 7, 1, 1]
    assert gandalf_vs_saruman(gandalf_spells, saruman_spells) == "GANDALF WINS"


def test_empty_spells():
    gandalf_spells = []
    saruman_spells = []
    assert gandalf_vs_saruman(gandalf_spells, saruman_spells) == "NO WINNER"
