f = open('input.txt', 'r')
directions = f.read()
santa_position_x = 0
santa_position_y = 0
robot_position_x = 0
robot_position_y = 0
visited = {0:[0]}
for index, direction in enumerate(directions):
    x = 0
    y = 0
    if index % 2 == 0:
        if direction == '<':
            santa_position_x-= 1
        elif direction == '>':
            santa_position_x+= 1
        elif direction == '^':
            santa_position_y -= 1
        elif direction == 'v':
            santa_position_y += 1
        x = santa_position_x
        y = santa_position_y
    else:
        if direction == '<':
            robot_position_x-= 1
        elif direction == '>':
            robot_position_x+= 1
        elif direction == '^':
            robot_position_y -= 1
        elif direction == 'v':
            robot_position_y += 1
        x = robot_position_x
        y = robot_position_y
    if x in visited:
        if y not in visited[x]:
            visited[x].append(y)
    else:
        visited[x] = [y]
print visited

total_houses = 0
for value in visited.values():
    print value
    total_houses += len(value)

print str(total_houses)