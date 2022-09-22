#7
def is_even(n):
  if n % 2 == 0:
    return True
  else:
    return False
print(is_even(42))

def is_even_short(n):
  return n % 2 == 0
#8
def is_odd(n):
  if n % 2 == 0:
    return False
  else:
    return True
print(is_odd(42))

#10
def is_rightangled(a,b,c):
  lhs = (b*b) + (a*a)
  rhs = c*c
  if lhs == rhs:
    return True
  else:
    return False
print(is_rightangled(3,4,5))
#11
def is_rightangled(a,b,c):
  L=0
  M=0
  S=0
  if a>=b and b>=c:
    L = a
    M = b
    S = c
  elif b>=c and c>=a:
    L = b
    M = c
    S = a
  elif c>=a and a>=b:
    L = c
    M = a
    S = b
  lhs = (M*M) + (S*S)
  rhs = L*L
  if lhs == rhs:
    return True
  else:
    return False
print(is_rightangled(3,3,2))


#hello_name
def hello_name(name):
  return "Hello " + name + "!"
print(hello_name("Walter White"))

#make_out_word
def make_out_word(out, word):
  return out[0:2] + word + out[2:]
print(make_out_word("<<>>","Arrows"))

#first_two
def first_two(str):
  return str[0:2]
print(first_two("bartholomew"))