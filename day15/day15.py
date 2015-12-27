import re

f = open("input.txt", "r")
name_regex = re.compile("([a-zA-Z]*)")
values_regex = re.compile("(-?\d+)")
ingredients = {}

line = f.readline()
while line != '':
    name = name_regex.match(line).group()
    ingredients[name] = [int(x) for x in values_regex.findall(line)]
    line = f.readline()
    
print ingredients
max_value_1 = 0
max_value_2 = 0
for i in ([w, x, y, z] for w in range(0,101) for x in range(0,101) if x+w <= 100 for y in range(0,101) if x+w+y <= 100 for z in range(0,101) if x+w+y+z == 100):
    totals = [0, 0, 0, 0]
    total_calories = 0
    j = 0
    for name, values in ingredients.iteritems():
        totals[0] += values[0] * i[j]
        totals[1] += values[1] * i[j]
        totals[2] += values[2] * i[j]
        totals[3] += values[3] * i[j]
        total_calories += values[4] * i[j]
        j += 1
    result = 1
    for total in totals:
        if total < 0:
            result = 0
        else:
            result *= total
    if result > max_value_1:
        max_value_1 = result
    if total_calories == 500 and result > max_value_2:
        max_value_2 = result
        
    
print "Best score: " + str(max_value_1)
print "Best 500 calories score: " + str(max_value_2)