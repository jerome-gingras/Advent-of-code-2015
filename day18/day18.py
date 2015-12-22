def count_neighbors_on(matrix, lineIndex, columnIndex, width, height):
    on_neighbors = 0
    if lineIndex > 0:
        # up
        if matrix[lineIndex-1][columnIndex]:
            on_neighbors += 1
        #up_left
        if columnIndex > 0:
            if matrix[lineIndex-1][columnIndex-1]:
                on_neighbors += 1
        #up_right
        if columnIndex < width-1:
            if matrix[lineIndex-1][columnIndex+1]:
                on_neighbors += 1
    if lineIndex < height-1:
        #down
        if matrix[lineIndex+1][columnIndex]:
            on_neighbors += 1
        #down_left
        if columnIndex > 0:
            if matrix[lineIndex+1][columnIndex-1]:
                on_neighbors += 1
        #down_right
        if columnIndex < width-1:
            if matrix[lineIndex+1][columnIndex+1]:
                on_neighbors += 1
    #right
    if columnIndex < width-1:
        if matrix[lineIndex][columnIndex+1]:
            on_neighbors += 1
    #left
    if columnIndex > 0:
        if matrix[lineIndex][columnIndex-1]:
            on_neighbors += 1
            
    return on_neighbors

def step_1(matrix, width, height):
    newValues = [row[:] for row in matrix][:]
    for lineIndex, line in enumerate(matrix):
        for columnIndex, light in enumerate(line):
            on_neighbors = count_neighbors_on(matrix, lineIndex, columnIndex, width, height)
            
            if light:
                if on_neighbors < 2 or on_neighbors > 3:
                    newValues[lineIndex][columnIndex] = False
            else:
                if on_neighbors == 3:
                    newValues[lineIndex][columnIndex] = True
    return newValues
    
def step_2(matrix, width, height):
    newValues = [row[:] for row in matrix][:]
    for lineIndex, line in enumerate(matrix):
        for columnIndex, light in enumerate(line):
            on_neighbors = count_neighbors_on(matrix, lineIndex, columnIndex, width, height)
            
            if lineIndex != 0 and lineIndex != height-1 or columnIndex != 0 and columnIndex != width-1:
                if light:
                    if on_neighbors < 2 or on_neighbors > 3:
                        newValues[lineIndex][columnIndex] = False
                else:
                    if on_neighbors == 3:
                        newValues[lineIndex][columnIndex] = True
    return newValues

f = open("input.txt", "r")
width = 100
height = 100
lights_1 = [[False for i in xrange(width)] for j in xrange(height)]
line = f.readline()
lineIndex = 0

#Setup grid
while line != "":
    for index, value in enumerate(line):
        if value == '#':
            lights_1[lineIndex][index] = True
    line = f.readline()
    lineIndex += 1
    
lights_2 = [row[:] for row in lights_1][:]

lights_2[0][0] = True
lights_2[0][width-1] = True
lights_2[height-1][0] = True
lights_2[height-1][width-1] = True

for i in xrange(100):
    lights_1 = step_1(lights_1, width, height)
    lights_2 = step_2(lights_2, width, height)
    
count_1 = 0
for line in lights_1:
    for light in line:
        if light:
            count_1 += 1
count_2 = 0
for line in lights_2:
    for light in line:
        if light:
            count_2 += 1
            
print "Final lights_1 on: %s" % count_1
print "Final lights_2 on: %s" % count_2