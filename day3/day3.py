f = open('input.txt', 'r')
directions = f.read()
position_x = 0
position_y = 0
visited = {0:[0]}
for direction in directions:
    if direction == '<':
        position_x -= 1
    elif direction == '>':
        position_x += 1
    elif direction == '^':
        position_y -= 1
    elif direction == 'v':
        position_y += 1
    if position_x in visited:
        if position_y not in visited[position_x]:
            visited[position_x].append(position_y)
    else:
        visited[position_x] = [position_y]
print visited

total_houses = 0
for value in visited.values():
    print value
    total_houses += len(value)

print str(total_houses)