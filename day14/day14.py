f = open("day14.txt", "r")

line = f.readline()
raindeers = {}

speed_index = 0
fly_index = 1
rest_index = 2
distance_index = 3
flying_index = 4
lastswitch_index = 5
points_index = 6

while line != '':
	(name, _, _, speed, _, _, fly_time, _, _, _, _, _, _, rest_time, _) = line.split()
	speed = int(speed)
	fly_time = int(fly_time)
	rest_time = int(rest_time)
	raindeers[name] = [speed, fly_time, rest_time, 0, False, 0, 0]
	line = f.readline()

for i in xrange(2503):
	leaders = []
	leader_distance = 0
	for key, raindeer in raindeers.iteritems():
		if raindeer[flying_index]:
			if ((i - raindeer[lastswitch_index]) % raindeer[fly_index]) == 0:
				raindeer[flying_index] = False
				raindeer[lastswitch_index] = i
		else:
			if ((i - raindeer[lastswitch_index]) % raindeer[rest_index]) == 0:
				raindeer[flying_index] = True
				raindeer[lastswitch_index] = i

		if raindeer[flying_index]:
			raindeer[distance_index] += raindeer[speed_index]

		if raindeer[distance_index] > leader_distance:
			leaders = [key]
			leader_distance = raindeer[distance_index]
		elif raindeer[distance_index] == leader_distance:
			leaders.append(key)

	for name in leaders:
		raindeers[name][points_index] += 1

print raindeers	
winner_distance = max(map(lambda x: x[distance_index], raindeers.values()))
winner_points = max(map(lambda x: x[points_index], raindeers.values()))
print "Winner distance: " + str(winner_distance)
print "Winner points: " + str(winner_points)