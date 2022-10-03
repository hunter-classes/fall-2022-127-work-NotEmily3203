def average(list):
  x = 0
  y = 0
  for i in list:
    x = x + i
    y = y+1
  return x/y

numbers = [1,2,3,4,5]
print(average(numbers))

def sum_of_squares(xs):
  x = 0
  for i in xs:
    x = x + (i * i)
  return x

print(sum_of_squares(numbers))