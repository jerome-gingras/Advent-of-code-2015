import re
f = open("input.txt")

regex = re.compile("\d{1,3},\d{1,3}")
line = f.readline()
lights = [[False for col in range(1000)] for row in range(1000)]

while line != '':
	positions = regex.findall(line)
	start_x, start_y = [int(x) for x in positions[0].split(',')]
	end_x, end_y = [int(x) for x in positions[1].split(',')]
	if line.startswith("turn on"):
		for i in xrange(start_x, end_x+1):
			for j in xrange(start_y, end_y+1):
				lights[i][j] = True
	elif line.startswith("turn off"):
		for i in xrange(start_x, end_x+1):
			for j in xrange(start_y, end_y+1):
				lights[i][j] = False
	elif line.startswith("toggle"):
		for i in xrange(start_x, end_x+1):
			for j in xrange(start_y, end_y+1):
				lights[i][j] = not lights[i][j]
	line = f.readline()

count = 0
for i in lights:
	for j in i:
		if j:
			count += 1
print "Result: " + str(count)