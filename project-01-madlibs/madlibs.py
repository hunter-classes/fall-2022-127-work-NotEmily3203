f = open("data.dat")
data = f.read()
words_from_data = data.split()
lines_from_data = data.split("/n")
stripped = []
for line in lines_from_data:
  stripped.append(line.strip())
print(data)
line = f.readline()
f.close()