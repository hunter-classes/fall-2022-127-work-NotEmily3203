def bondify(name):
  space_location = name.find(" ")
  f = name[0:space_location]
  l = name[space_location+1:]
  return l + ", " + f + " " + l
print(bondify("Emily Lin"))

def piglatin(word):
  list=["A","E","I","O","U"]
  for i in list:
    if word[0].upper() == i:
      return word + "yay"
  if word[0].upper() != i:
     return word[1:] + word[0] + "ay"
print(piglatin("breach"))