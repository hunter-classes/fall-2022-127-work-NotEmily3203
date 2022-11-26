"""
EXTRAS:
-Store your translations in a file named pirate.dat the file should have lines in the form “word:translation.”
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
  if i in klist:
    index = words.index(i)
    words[index] = i.replace(i,pirate[i])
translate = " ".join(words)
print("before: ",story)
print("after: ",translate)