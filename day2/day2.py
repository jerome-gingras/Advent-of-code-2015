f = open('input.txt', 'r')
line = f.readline()
total_required_paper = 0
total_required_ribbon = 0

while line != '':
	sizes = line.split('x')
	l = int(sizes[0])
	w = int(sizes[1])
	h = int(sizes[2])
	sortedSizes = sorted([l,w,h])
	required = 2*l*w + 2*w*h + 2*h*l + sortedSizes[0] * sortedSizes[1]
	total_required_paper += required
	total_required_ribbon += 2*sortedSizes[0] + 2*sortedSizes[1] + l*w*h
	line = f.readline()
print 'required paper = ' + str(total_required_paper)
print 'required ribbon = ' + str(total_required_ribbon)