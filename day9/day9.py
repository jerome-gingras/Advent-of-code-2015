from itertools import permutations
import sys

f = open("C:\\Dev\\Advent-of-code-2015\\day9\\input.txt", "r")
line = f.readline()
cities = set()
distances = dict()
while line != "":
    (source, _, destination, _, distance) = line.split()
    cities.add(source)
    cities.add(destination)
    if source in distances:
        distances[source][destination] = int(distance)
    else:
        distances[source] = dict([(destination, int(distance))])
    if destination in distances:
        distances[destination][source] = int(distance)
    else:
        distances[destination] = dict([(source, int(distance))])
    line = f.readline()

shortest_path = sys.maxint
longest_path = 0

for items in permutations(cities):
    distance = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
    shortest_path = min(shortest_path, distance)
    longest_path = max(longest_path, distance)

print "Shortest path is " + str(shortest_path)
print "Longuest path is " + str(longest_path)