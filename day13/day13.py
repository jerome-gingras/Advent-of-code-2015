import sys
from itertools import permutations

def calculate_arrangement(people, changes):
	most_happiness = -sys.maxint-1
	for i in permutations(people):
		happiness = sum(map(lambda x, y: changes[x][y] + changes[y][x], i[:-1], i[1:]))
		happiness += changes[i[-1]][i[0]] + changes[i[0]][i[-1]]
		most_happiness = max(most_happiness, happiness)

	return most_happiness

f = open('day12.txt', 'r')
people = set()
changes = dict()

line = f.readline()
while line != '':
	parts = line.strip().split(' ')
	source = parts[0]
	direction = -1 if parts[2] == "lose" else 1
	change = int(parts[3])
	destination = parts[10].strip('.')
	people.add(source)
	people.add(destination)
	changes.setdefault(source, {})
	changes[source][destination] = change * direction
	line = f.readline()

print "Most happiness without me: " + str(calculate_arrangement(people, changes))

changes.setdefault('me', {})
for i in changes:
	changes['me'][i] = 0
	changes[i]['me'] = 0
people.add('me')

print "Most happiness with me: " + str(calculate_arrangement(people, changes))