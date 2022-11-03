"""
EXTRAS:
-Instead of specifying the sentences or story to convert, write a story in a file and read it from your program. Make sure to include the file in your repo and that your program reads it correctly.
-Add some replacements that are unique, that is, the first time you see them you select on randomly but then you keep reusing that replacement.
-Pay attention to letter case. That is, if you replace a word at the beginning of a sentence, it should be capitalized, otherwise, lowercase. This is except in the case of proper nouns which should always be capitalized.
"""

import random

villain = [" the radioactive cockroch","the mutant rat","the poisonous lanternfly","the poopy pigeon","the super-crackhead","the hawky 🦅"]
verb = ["dance with","punch","kick","jump on","kiss","flirt with","grab","slap","headbutt"]
noun = ["pistol","katana","stick","book","cigarette butt"]
feelings = ["confused","happy","annoyed","angry","flustered","turned on","digusted","flabbergasted","bamboozled","in Ohio"]
heroes = ["Spider-man", "Jungkook from BTS", "Superman", "Queen Elization (undead)", "Jimin from BTS", "The Powerpuff Girls","Batman"]

randvillain = random.choice(villain)
randnoun = random.choice(noun)
randheroes = random.choice(heroes)


f = open("data.dat")
for x in f:
  x = x.split()
  for i in x:
    if i == "<villain>":
      if x.index("<villain>") != 0:
        randvillain = randvillain.lower()
      else:
        randvillain = randvillain.capitalize()
  x = ' '.join(x)
  x = x.replace('<villain>',randvillain)
  x = x.replace('<noun>',randnoun)
  x = x.replace('<damage>',str(random.randrange(0,30,5)))
  x = x.replace('<verb>',random.choice(verb))
  x = x.replace('<feelings>',random.choice(feelings))
  x = x.replace('<hero>',randheroes)
  print(x)