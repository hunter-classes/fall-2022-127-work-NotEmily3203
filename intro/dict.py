s = """bing bong
king kong
ting tong
"""

def count_letters(s):
  counts = {}
  for letter in s:
    if letter in counts.keys():
      counts[letter] = counts[letter] + 1
    else:
      counts[letter] = 1
  return counts

def count_words(s):
  counts = {}
  for word in s.split():
    if word in counts.keys():
      counts.setdefault(word,0) #if word not in dictionary, add word and set it to 0, this is useful for checking word
      counts[word] = counts[word] + 1
    else:
      counts[word] = 1
  return counts
