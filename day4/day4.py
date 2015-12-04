import md5
input = "ckczppom"
found_1 = False
found_2 = False
result_1 = 0
result_2 = 0
i = 1

while not (found_1 and found_2):
	temp = input + str(i)
	digest = md5.new(temp).digest().encode("hex")
	if (not found_1) and digest.startswith("00000"):
		found_1 = True
		result_1 = i
	elif (not found_2) and digest.startswith("000000"):
		found_2 = True
		result_2 = i
	i += 1
print "result 1: " + str(result_1)
print "result 2: " + str(result_2)