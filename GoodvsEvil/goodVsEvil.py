goodValues = [1, 2, 3, 3, 4, 10]
evilValues = [1, 2, 2, 2, 3, 5, 10]


def calculate_army_Value(army, values):
    force = sum(int(resource) * value for resource,
                value in zip(army.split(" "), values))
    return force


def goodVsEvil(good, evil):
    goodArmy = calculate_army_Value(good, goodValues)
    evilArmy = calculate_army_Value(evil, evilValues)

    if evilArmy > goodArmy:
        return "Battle Result: Evil eradicates all trace of Good"
    elif goodArmy > evilArmy:
        return "Battle Result: Good triumphs over Evil"
    return "Battle Result: No victor on this battle field"
