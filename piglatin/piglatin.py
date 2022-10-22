def bondify(name):
  space_location = name.find(" ")
  f = name[0:space_location]
  l = name[space_location+1:]
  return l + ", " + f + " " + l

def piglatin(word):
  punctuation = ""
  if word[-1] == "." or word[-1] == "!" or word[-1] == "?":
    punctuation = word[-1]
    word = word.replace(word[-1],"")
  vowels=["A","E","I","O","U"]
  for i in vowels:
    if word[0].upper() == i:
      return word + "yay" + punctuation
    if word[0].upper() != i:
      if word[0] == word[0].upper():
        capital = word[1:].uppercase()
      else:
        capital = word[1:]
  return capital + word[0].lower() + "ay" + punctuation
      
print(piglatin("understood?"))