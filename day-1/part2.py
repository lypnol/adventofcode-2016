
x,y,o = 0,0,"N" # position and orientation
visited = []
min_visited = float("inf")
commands = []
with open("input.txt") as f:
    commands = f.read().split(", ")

for c in commands:
    direction = c[0]
    distance = int(c[1:])
    if o == "N":
        if direction == "R":
            o = "E"
            for i in range(x, x+distance): visited.append((i, y))
            x += distance
        else:
            o = "W"
            for i in range(x, x-distance, -1): visited.append((i, y))
            x -= distance
    elif o == "S":
        if direction == "R":
            o = "W"
            for i in range(x, x-distance, -1): visited.append((i, y))
            x -= distance
        else:
            o = "E"
            for i in range(x, x+distance): visited.append((i, y))
            x += distance
    elif o == "W":
        if direction == "R":
            o = "N"
            for i in range(y, y+distance): visited.append((x, i))
            y += distance
        else:
            o = "S"
            for i in range(y, y-distance, -1): visited.append((x, i))
            y -= distance
    elif o == "E":
        if direction == "R":
            o = "S"
            for i in range(y, y-distance, -1): visited.append((x, i))
            y -= distance
        else:
            o = "N"
            for i in range(y, y+distance): visited.append((x, i))
            y += distance
for i, (x,y) in enumerate(visited):
    if (x,y) in visited[:i]+visited[i+1:] and min_visited > abs(x)+abs(y):
        min_visited = abs(x)+abs(y)

print(min_visited)
