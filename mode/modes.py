def findLargest(l):
  s = l[0]
  print(s)
  x = [x for x in l if x > s]
  return x
lst = [100,10,1,10000,9,1]
print(findLargest(lst))
def freq(l,v):
  count = [i for i in l if i == v]
  print(count)
  return count
print(freq(lst,1))