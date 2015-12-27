import re
import json

def solve_1(input):
    sum = 0
    for i in re.findall("-?\d+", input):
        sum += int(i)
    return sum

def sum_numbers(object):
    sum = 0
    if isinstance(object, int):
        return object
    if isinstance(object, (str, unicode)):
        return 0
    if isinstance(object, list):
        for i in object:
            sum += sum_numbers(i)
        return sum
    else: # a dict
        for key,value in object.iteritems():
            if isinstance(value, (str, unicode)) and value == u"red":
                return 0
            else:
                sum += sum_numbers(value)
    return sum
    
def solve_2(input):
    object = json.loads(input)
    return sum_numbers(object)
    
f = open("input.txt")
input_content = f.readline()

print "Sum of all the numbers: " + str(solve_1(input_content))

print "Sum of all the numbers with no red property: " + str(solve_2(input_content))