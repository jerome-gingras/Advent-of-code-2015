problem_input = "3113322113"

def partition(input, iterations):
    output = []
    for i in xrange(iterations):
        last = input[0]
        count = 1
        output = []
    
        for c in input[1:]:
            if c == last:
                count += 1
            else:
                output.append(str(count))
                output.append(last)
                last = c
                count = 1
        output.append(str(count))
        output.append(last)
        input = ''.join(output)
    return input


output = partition(problem_input, 40)
print "Length of 40 iterations output: " + str(len(output))

output = partition(output, 10)
print "Length of 50 iterations output: " + str(len(output))
