import random
villain = ["Radioactive Cockroch","Mutant Rat","Poisonous Lanternfly","Poopy Pigeon","Super-Crackhead"]
aggroverb = ["run","dance","punch","kick","jump","kiss","flirt","grab"]
weapon = ["pistol","katana","stick",""]

randvillain = random.choice(villain).capitalize()
randverb = random.choice(aggroverb).capitalize()
randwep = random.choice(weapon).capitalize()
randdamage = random.randrange(0,30,5)

f = open("data.dat")
for x in f:
  x = x.replace('>',randvillain)
  x = x.replace('_',randverb)
  x = x.replace('-',randwep)
  x = x.replace('#',randdamage)
  print(x)
#f.seek(0)
#line = f.readline()
