import random
def findLargest(l):
  s = l[0]
  for i in l:
    if i > s:
      s = i
  return s
lst = [100,10,1,10000,9,1]
print(findLargest(lst))

def freq(l,v):
  x = [i for i in l if i == v]
  count = len(x)
  return count
print(freq(lst,1))

def buildRandomList(size,maxvalue):
    result = []
    for i in range(size):
      result.append(random.randrange(5))
    return result


def mode(dataset):
    """
    Returns a mode of the dataset, that is
    the value that appears most frequently
    if multiple values appear the same # of times and are
    most frequent, return any of them.
    Ex: mode([5,4,5,6,7,8,5,4]) --> 5 since 5 appears the     most
    Ex: mode([5,5,5,4,4,4,2,2,7,7,8,8,9]) --> return 5 or 4   since both of those values appear 3 times which is the    most
    Strategy:
    assume the first value is the mode
    we can grab its frequency
    for each remaining item in the dataset:
    count that items frequence and see if it's the new
    mode so far    
    """
    modeSoFar = dataset[0]
    freqSoFar = dataset.count(modeSoFar)
    for item in dataset[1:]: #outer loop -> n
        # calling freq each time is n
        # if freq(dataset,item) > freqSoFar:
        if dataset.count(item) > freqSoFar:
            modeSoFar = item
            freqSoFar = dataset.count(item)
    return modeSoFar


slot = []
for i in range(1000):
  slot.append(random.randrange(0,100))
def fastMode(dataset):
    # assume all values in dataset
    # are between 0 and 99 inclusive
    # 1. make a list of 100 slots
    # and set them all to 0
    # this will store our tallies
  tallies = []
  for i in range(100):
    tallies.append(0)
    # 2. Loop through our dataset
    # and for each item incremement
    # (add 1) to the appropriate
    # slot in the tallies list
  for i in dataset:
    tallies[i] += 1
    # 3. the index with the highest
    # value in tallies is the mode
  return findLargest(tallies)

print(fastMode(slot))