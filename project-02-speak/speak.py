"""
EXTRAS:
-Store your translations in a file named pirate.dat the file should have lines in the form “word:translation.”
- Handle upper and lower case and punctuation
"""
#puts translation into dict
pirate = {}
f = open("pirate.dat")
lines = f.read()
perline = lines.split("\n")
for i in perline:
  index = i.rfind(":")
  pirate[i[0:index]]=i[index+1:]

klist = [x for x in pirate.keys()]

s = open("input.txt")
story = s.read()
words = story.split(" ")
print(words)
for i in words:
  x = 0
  if i.isalpha() == False:
    e = i[0:-1]
    p = i[-1:]
    x = 1
  else:
    e = i
  if e in klist:
    index = words.index(i)
    if i == i.capitalize(): #checks if word is capitalized
      words[index] = i.replace(i,pirate[e].capitalize())
    else:
      words[index] = i.replace(i,pirate[e])
    if x == 1:
      words[index] += p
translate = " ".join(words)
print("before: ",story)
print("after: ",translate)