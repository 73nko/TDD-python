def in_array(array1, array2):
    result = []
    for word in array1:
        for possible_substring in array2:
            if word in possible_substring:
                result.append(word)
                break
    return sorted(list(dict.fromkeys(result)))
