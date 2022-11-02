"""
EXTRAS:
-Instead of specifying the sentences or story to convert, write a story in a file and read it from your program. Make sure to include the file in your repo and that your program reads it correctly.
-Add some replacements that are unique, that is, the first time you see them you select on randomly but then you keep reusing that replacement.
"""

import random

villain = [" the radioactive cockroch","the mutant rat","the poisonous lanternfly","the poopy pigeon","the super-crackhead","the Hawky 🦅","the Florida man"]
hero = [""]
verb = ["dance with","punch","kick","jump on","kiss","flirt with","grab","slap","headbutt"]
noun = ["pistol","katana","stick","book","cigarette butt"]
feelings = ["confused","happy","annoyed","angry","flustered","turned on","digusted","flabbergasted","bamboozled","in Ohio"]

randvillain = random.choice(villain)
randnoun = random.choice(noun)

f = open("data.dat")
for x in f:
  x = x.replace('<villain>',randvillain)
  x = x.replace('-',randnoun)
  x = x.replace('#',str(random.randrange(0,30,5)))
  x = x.replace('_',random.choice(verb))
  x = x.replace('^',random.choice(feelings))
  print(x)