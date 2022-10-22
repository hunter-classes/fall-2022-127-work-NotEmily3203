def initialize(name):
  space_location = name.find(" ")
  f = name[0].upper()
  l = name[space_location+1:].uppercase()
  return f + ". " + l
print(initialize("Emily Lin"))