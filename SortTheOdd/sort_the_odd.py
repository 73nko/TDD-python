def sort_array(arr):
  odds = sorted(filter(lambda n: n % 2 != 0, arr))
  return [odds.pop(0) if n%2 != 0 else n for n in arr]
