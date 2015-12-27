import sys
global minimum_length, minimum_count
minimum_length = sys.maxint
minimum_count = 0

def get_combinations(previous, array, target):
    global minimum_length
    global minimum_count
    possible = []
    if len(array) < 1:
        return possible
    value = array[0]
    newArray = array[1:]
    # try without this one
    possible.extend(get_combinations(previous[:], newArray, target))
    if value < target:
        target = target-value
        previous.append(value)
        # find the rest when this one is in
        possible.extend(get_combinations(previous, newArray, target))
    elif value == target:
        previous.append(value)
        possible.append(previous)
        if len(previous) < minimum_length:
            minimum_length = len(previous)
            minimum_count = 1
        elif len(previous) == minimum_length:
            minimum_count += 1
    return possible

f = open("input.txt", "r")
containers = []
line = f.readline()
while line != "":
    containers.append(int(line))
    line = f.readline()

combinations = []    
#for index, value in enumerate(containers):
combinations.extend(get_combinations([], containers[0:], 150))

print "Number of combinations: %s" % len(combinations)
print "Minimal lenght of combinations: %s " % minimum_length
print "Number of combinations with the minimum length: %s" % minimum_count