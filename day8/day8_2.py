import re

hex_characters = re.compile(r"\\x[a-f0-9]{2}")

f = open("input.txt", "r")
line = f.readline()
literal_count = 0
encoded_count = 0
while line != '':
    line = line.strip()
    literal_count += len(line)
    line = ("aaa" + line[1:-1] + "aaa").replace("\\\"", "bbbb").replace("\\\\", "cccc")
    hex_characters_count = len(hex_characters.findall(line))
    encoded_count += len(line) + hex_characters_count
    line = f.readline()

print "Literal characters = " + str(literal_count)
print "Encoded characters = " + str(encoded_count)
print "Difference = " + str(encoded_count - literal_count)

f.close()