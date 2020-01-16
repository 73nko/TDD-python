def reverse_words(text):
  words = text.split(" ")
  result = [word[::-1] for word in words] 
  return " ".join(result)
