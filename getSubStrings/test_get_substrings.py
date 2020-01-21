from get_substrings import in_array


def test_inarray():
    # given two empty arrays returns an empty array
    arr1 = []
    arr2 = []
    result = []
    assert in_array(arr1, arr2) == result


def test_find_substrings():
    # given a substring, returnss that word.
    arr1 = ["live"]
    arr2 = ["lively"]
    result = ["live"]
    assert in_array(arr1, arr2) == result


def test_find_substrings_and_break():
    # given two words which one substring, find that substring.
    arr1 = ["live"]
    arr2 = ["lively", "alive"]
    result = ["live"]
    assert in_array(arr1, arr2) == result


def test_find_several_substrings():
    # find all the substrings in the arrays
    arr1 = ["arp", "live", "strong"]
    arr2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    result = ["arp", "live", "strong"]
    assert in_array(arr1, arr2) == result


def test_return_the_result_sorted():
    arr1 = ["live", "arp", "strong"]
    arr2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    result = ['arp', 'live', 'strong']
    assert in_array(arr1, arr2) == result


def test_remove_duplicates():
    arr1 = ["live", "arp", "strong", "live"]
    arr2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    result = ['arp', 'live', 'strong']
    assert in_array(arr1, arr2) == result
