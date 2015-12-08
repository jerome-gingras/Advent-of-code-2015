import re

hex_characters = re.compile(r"\\x[a-f0-9]{2}")

f = open("input.txt", "r")
line = f.readline()
literal_count = 0
memory_count = 0
while line != '':
    line = line.strip()
    literal_count += len(line)
    line = line[1:-1]
    #replace so that the other regex doesn't catch false \xff
    line = line.replace("\\\"", "a")
    line = line.replace("\\\\", "b")
    hex_characters_count = len(hex_characters.findall(line))
    memory_count += len(line) - hex_characters_count * 3
    line = f.readline()

print "Literal characters = " + str(literal_count)
print "In-memory characters = " + str(memory_count)
print "Difference = " + str(literal_count - memory_count)

f.close()