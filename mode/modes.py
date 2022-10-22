def findLargest(l):
  s = l[0]
  x = [x for x in l if x > s]
  return x
lst = [100,10,1,10000,9,1]
print(findLargest(lst))
def freq(l,v):
  x = [i for i in l if i == v]
  count = len(x)
  return count
print(freq(lst,1))