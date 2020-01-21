def binary_array_to_number(arr):
    result = 0
    for i, num in enumerate(arr[::-1]):
        if num:
            result += 2 ** i
    return result


binary_array_to_number([0, 0, 1, 0])
