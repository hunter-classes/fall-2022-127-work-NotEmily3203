"""
EXTRAS:
-Instead of specifying the sentences or story to convert, write a story in a file and read it from your program. Make sure to include the file in your repo and that your program reads it correctly.
-Add some replacements that are unique, that is, the first time you see them you select on randomly but then you keep reusing that replacement.
"""

import random

villain = ["radioactive cockroch","mutant rat","poisonous lanternfly","poopy pigeon","super-crackhead","Hawky 🦅","Florida man"]
aggroverb = ["dance with","punch","kick","jump on","kiss","flirt with","grab","slap","headbutt"]
weapon = ["pistol","katana","stick","book","cigarette butt"]
feelings = ["confused","happy","annoyed","angry","flustered","turned on","digusted","flabbergasted","bamboozled","in Ohio"]

randvillain = random.choice(villain)
randwep = random.choice(weapon)

f = open("data.dat")
for x in f:
  x = x.replace('>',randvillain)
  x = x.replace('-',randwep)
  x = x.replace('#',str(random.randrange(0,30,5)))
  x = x.replace('_',random.choice(aggroverb))
  x = x.replace('^',random.choice(feelings))
  print(x)