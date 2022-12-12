"""
EXTRAS:
- Use more than one data source and have your analysis compare,contrast, or correlate them
- Use multiple aspects of a single data source in your analysis
"""
import csv
"""
Which is healthier, starbucks or cereal??
In order to figure this out, we will be averaging the nutrition
values for the menu.
"""

#read the data
c = open("cereal.csv")
s = open("starbucks-menu-nutrition-drinks.csv")

#clean cereal.csv and get values
cereal = csv.reader(open("cereal.csv"))
citems = 0
ccalories = 0
cprotein = 0
cfat = 0
csodium = 0
cfiber = 0
ccarbs = 0
for line in cereal:
  line.pop(1)
  line.pop(1)
  line.pop(7)
  line.pop(7)
  line.pop(7)
  line.pop(7)
  line.pop(7)
  line.pop(7)
  line.pop(7)
  citems += 1
  ccalories += int(float(line[1]))
  cprotein += int(float(line[2]))
  cfat += int(float(line[3]))
  csodium += int(float(line[4]))
  cfiber += int(float(line[5]))
  ccarbs += int(float(line[6]))

#get starbucks-menu-nutrition-drinks.csv values
starbucks = csv.reader(open("starbucks-menu-nutrition-drinks.csv"))
sitems = 0
scalories = 0
sprotein = 0
sfat = 0
ssodium = 0
sfiber = 0
scarbs = 0
for line in starbucks:
  if "-" in line:
    continue
  sitems += 1
  scalories += int(float(line[1]))
  sfat += int(float(line[2]))
  scarbs += int(float(line[3]))
  sfiber += int(float(line[4]))
  ssodium += int(float(line[5]))
  sprotein += int(float(line[6]))

#function to find average
def avg(items, nutrition):
  avg = nutrition/items
  return avg

#comparison time
starbucks = 0
if avg(sitems, scalories) < avg(citems, ccalories):
  starbucks += 1
if avg(sitems, sfat) < avg(citems, cfat):
  starbucks += 1
if avg(sitems, scarbs) < avg(citems, ccarbs):
  starbucks += 1
if avg(sitems, sfiber) > avg(citems, cfiber):
  starbucks += 1
if avg(sitems, ssodium) < avg(citems, csodium):
  starbucks += 1
if avg(sitems, sprotein) > avg(citems, cprotein):
  starbucks += 1
#The number 3 is chosen because we are comparing 6 nutritions, if starbucks is better than cereal, then it should earn a point in over 3 categories.
if starbucks < 3:
  print("cereal is healthier in general")
elif starbucks == 3:
  print("they equally suck")
else:
  print("starbucks is healthier in general")