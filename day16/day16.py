import re

f = open("input.txt", "r")
infos_regex = re.compile(r"([a-zA-Z]+: \d+)")
sues = []
correct_infos = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
correct_sue_1 = -1
correct_sue_2 = -1
line = f.readline()
while line != '':
    infos = infos_regex.findall(line)
    sue = {}
    is_good_1 = True
    is_good_2 = True
    for info in infos:
        parts = info.split(": ")
        name = parts[0]
        value = int(parts[1])
        sue[name] = value
        # Part 1
        if not correct_infos[name] == value:
            is_good_1 = False
            
        # Part 2
        if name == "trees" or name == "cats":
            if not correct_infos[name] < value:
                is_good_2 = False
        elif name  == "pomeranians" or name == "goldfish":
            if not correct_infos[name] > value:
                is_good_2 = False
        elif not correct_infos[name] == value:
            is_good_2 = False
    sues.append(sue)
    if is_good_1:
        correct_sue_1 = len(sues)
    if is_good_2:
        correct_sue_2 = len(sues)
    line = f.readline()
    
print "Right Sue's number: " + str(correct_sue_1)
print "Actual right Sue's number: " + str(correct_sue_2)