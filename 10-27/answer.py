def mode(lst):
  mode = lst[0]
  for i in lst:
    if lst.count(mode) < lst.count(i):
      mode = i
  return mode

list = [1,2,3,3,4,5,6,6,6,6,7,7,8]
print(mode(list))