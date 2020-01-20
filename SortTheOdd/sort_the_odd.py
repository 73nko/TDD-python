def sort_array(arr):
  odds = sorted(filter(lambda n: n % 2 != 0, arr))
  # I had reversed the sorted list at first. 
  # I've dicoveredt pop 0 and I think is more readable
  return [odds.pop(0) if n%2 != 0 else n for n in arr]
