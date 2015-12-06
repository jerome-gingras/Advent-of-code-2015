import re
f = open("input.txt")

regex = re.compile("\d{1,3},\d{1,3}")
line = f.readline()
lights = [[0 for col in range(1000)] for row in range(1000)]

while line != '':
	positions = regex.findall(line)
	start_x, start_y = [int(x) for x in positions[0].split(',')]
	end_x, end_y = [int(x) for x in positions[1].split(',')]
	if line.startswith("turn on"):
		for i in xrange(start_x, end_x+1):
			for j in xrange(start_y, end_y+1):
				lights[i][j] += 1
	elif line.startswith("turn off"):
		for i in xrange(start_x, end_x+1):
			for j in xrange(start_y, end_y+1):
				if lights[i][j] > 0:
					lights[i][j] -= 1
	elif line.startswith("toggle"):
		for i in xrange(start_x, end_x+1):
			for j in xrange(start_y, end_y+1):
				lights[i][j] += 2
	line = f.readline()

count = 0
for i in lights:
	for j in i:
		count += j
print "Result: " + str(count)