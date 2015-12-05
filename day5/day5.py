import re

vowelsRegex = re.compile(".*([aeiou].*){3,}.*")
doubleRegex = re.compile(".*([a-z])\\1+.*")
illegalWords = re.compile(".*((ab)|(cd)|(pq)|(xy)).*")

f = open("input.txt")
line = f.readline().replace("\n", "")
good_count = 0
while line != '':
	if vowelsRegex.match(line) != None:
		if doubleRegex.match(line) != None:
			if illegalWords.match(line) == None:
				good_count += 1
	line = f.readline().replace("\n", "")

print "Result: " + str(good_count)