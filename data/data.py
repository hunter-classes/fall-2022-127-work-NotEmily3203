"""
EXTRAS:
- Use Matplotlib or another Python graphing/plotting library to visualize part or all of your analysis
- Use more than one data source and have your analysis compare,contrast, or correlate them
- Use multiple aspects of a single data source in your analysis
"""

#which is healthier, starbucks or cereal??

#read the data
c = open("cereal.csv")
s = open("starbucks-menu-nutrition-drinks.csv")

#clean cereal.csv
lines = c.read()
cereals = lines.split("\n")
print(cereals)

# add each name to a dict as a key
# add each value as 

  