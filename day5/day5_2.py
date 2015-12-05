import re

doublePairsRegex = re.compile("^.*([a-z]{2}).*\\1+.*$")
repeatWithMiddleRegex = re.compile("^.*([a-z]).\\1+.*$")
f = open("input.txt")
line = f.readline().replace("\n", "")
good_count = 0
while line != '':
	if doublePairsRegex.match(line) != None:
		if repeatWithMiddleRegex.match(line) != None:
			good_count += 1
	line = f.readline().replace("\n", "")

print "Result: " + str(good_count)