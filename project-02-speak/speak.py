"""
EXTRAS:
-Store your translations in a file named pirate.dat the file should have lines in the form “word:translation.”
-Handle upper and lower case and punctuation
-Have an option to translate different languages (Pirate and Austro)
-Converting parts of words rather than straight substitutions
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
for i in words:
  x = 0
  if i.isalpha() == False:
    e = i[0:-1].lower()
    p = i[-1:]
    x = 1
  else:
    e = i.lower()
  if e in klist:
    index = words.index(i)
    if i == e.capitalize(): #checks if word is capitalized
      words[index] = i.replace(i,pirate[e].capitalize())
    else:
      words[index] = i.replace(i,pirate[e])
    if x == 1:
      words[index] += p
ptranslate = " ".join(words)

austro = {}
f = open("austro.dat")
lines = f.read()
perline = lines.split("\n")
for i in perline:
  index = i.rfind(":")
  austro[i[0:index]]=i[index+1:]

klist = [x for x in austro.keys()]

s = open("input.txt")
story = s.read()
words = story.split(" ")
for i in words:
  x = 0
  if i.isalpha() == False:
    e = i[0:-1].lower()
    p = i[-1:]
    x = 1
  else:
    e = i.lower()
  for l in klist:
    if l in e:
      windex = words.index(i)
      lindex = i.index(l)
      words[windex] = i.replace(i[lindex:lindex+len(l)],austro[l])
      if x == 1:
        words[index] += p
atranslate = " ".join(words)

print("ORIGINAL: ", story,"\n")
print("PIRATE: ",ptranslate,"\n")
print("AUSTRO: ",atranslate,"\n")