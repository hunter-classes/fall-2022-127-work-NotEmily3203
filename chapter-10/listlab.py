numbers = [1,3,4,6,3,6]
number = [4,5,7,3,2,0]
words = ["sam","dave","cthulu","sam","beezlebub"]
word = "eliminate"

def minimum(list):
  x = list[0]
  for i in list:
    if x > i:
      x = i
    else:
      pass
  return x

print(minimum(numbers))

def odd(list):
  oddlist = []
  for i in list:
    if i % 2 == 1:
      oddlist.append(i)
  return oddlist

print(odd(numbers))

def capitalized(word):
  return word.upper()

print(capitalized(word))

def five_upper(word):
  length = len(word)
  if length > 4:
    word = word.upper()
  return word

print(five_upper(word))

def squared(list):
  new_numbers = []
  for i in list:
    new = i*i
    new_numbers.append(new)
  return new_numbers

print(squared(numbers))

def add(list1, list2):
  list3 = []
  index = 0
  for i in list1:
    new = list1[index] + list2[index]
    index +=1
    list3.append(new)
  return list3

print(add(numbers, number))

def count(list):
  count = 0
  for i in list:
    if len(i) == 5:
      count += 1
  return count

print(count(words))

def sum(list):
  sum = 0
  x = 0
  while x == 0:
    for i in list:
      if i%2 == 0:
        x = 1
        break
      else:
        sum += i
  return sum

print(sum(numbers))

def occur(list):
  sam = list.count("sam")
  return sam
      
print(occur(words))