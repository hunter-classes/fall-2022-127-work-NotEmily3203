"""
EXTRAS:
-Instead of specifying the sentences or story to convert, write a story in a file and read it from your program. Make sure to include the file in your repo and that your program reads it correctly.
-Add some replacements that are unique, that is, the first time you see them you select on randomly but then you keep reusing that replacement.
-Pay attention to letter case. That is, if you replace a word at the beginning of a sentence, it should be capitalized, otherwise, lowercase. This is except in the case of proper nouns which should always be capitalized.
"""

import random

villain = ["Radioactive Cockroch","Mutant Rat","Poisonous Lanternfly","Poopy Pigeon","Super-Crackhead","Hawky 🦅","Florida Man"]
aggroverb = ["run","dance","punch","kick","jump","kiss","flirt","grab"]
weapon = ["pistol","katana","stick","improvised toilet stall","cigarette butt"]
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