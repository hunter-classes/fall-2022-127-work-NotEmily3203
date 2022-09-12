s1="double quote"
s2='single\nquote'
s3="""
this is a multiline string
we use triple quotes
"""

#use backslash to escape string
s4='john\'s book'

print(len(s1))
print(len("abcde"))
location = s1.find(" ")
print(location)
s5 = s1[location+1:]
print(s1[0:6])