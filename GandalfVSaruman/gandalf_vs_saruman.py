

def gandalf_vs_saruman(gandalf_spells, saruman_spells):
    result = "NO WINNER"
    g_wins = 0
    s_wins = 0
    last_winner = 0
    for index, spell in enumerate(gandalf_spells):
        if (spell > saruman_spells[index]):
            if (last_winner == 1):
                s_wins = 0
            g_wins += 1
            last_winner = 0

        elif (spell < saruman_spells[index]):
            if (last_winner == 1):
                g_wins = 0
            s_wins += 1
            last_winner = 1

        if (s_wins == 3 or g_wins == 3):
            break

    if (g_wins == 3):
        result = "GANDALF WINS"
    if (s_wins == 3):
        result = "SARUMAN WINS"

    return result


gandalf_spells = [2, 3, 4, 5, 6, 2, 2]
saruman_spells = [3, 4, 3, 7, 7, 5, 1]
gandalf_vs_saruman(gandalf_spells, saruman_spells)
