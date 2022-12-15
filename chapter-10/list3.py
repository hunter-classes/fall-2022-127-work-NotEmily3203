list = [1,5,2,7,3,9,6]

def max(numbers):
  x = numbers[0]
  for i in numbers:
    if x < i:
      x = i
    else:
      pass
  return x

print(max(list))

def odd(numbers):
  oddlist = []
  for i in numbers:
    if i % 2 == 1:
      oddlist.append(i)
  return oddlist

print(odd(list))

def even(numbers):
  evensum = 0
  for i in numbers:
    if i % 2 == 0:
      evensum += i
  return evensum

print(even(list))