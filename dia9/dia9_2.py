file = open("dia9/dia9.txt", "r")
#file.close()
#file = open("dia9/dia9_t.txt", "r")

data = []
visited = []
basins = []
w = 0
h = 0
for line in file:
    line = line.rstrip("\n")
    print(line)
    line = [int(x) for x in list(line)]
    _vl = []
    data.append(line)
    for j in line:
        if j == 9:
            _vl.append(True)
        else:
            _vl.append(False)
    visited.append(_vl)
    h += 1
w = len(data[0])
file.close()

for r in visited:
    for c in r:
        if not c:
            print(".", end="")
        else:
            print("1", end="")
    print("")

def bfs (x,y,basin_index):
    sides = []
    #inner elements
    if 0 < x and x < w - 1 and 0 < y and y < h - 1:
        if not visited[y][x-1]:
            sides.append([x-1, y])
        if not visited[y][x+1]:
            sides.append([x + 1, y])
        if not visited[y-1][x]:
            sides.append([x, y - 1])
        if not visited[y+1][x]:
            sides.append([x, y + 1])

    #corner
    if x == 0 and y == 0: # up left corner
        if not visited[1][0]:
            sides.append([1, 0])
        if not visited[0][1]:
            sides.append([0, 1])
    if x == w - 1 and y == 0:# up right corner
        if not visited[0][x - 1]:
            sides.append([x - 1, 0])
        if not visited[1][x]:
            sides.append([x, 1])
    if x == 0 and y == h - 1: #down left corner
        if not visited[y-1][0]:
            sides.append([0,y-1])
        if not visited[y][1]:
            sides.append([1,y])
    if x == w - 1 and y == h - 1: # down right corner
        if not visited[y][x-1]:
            sides.append([x-1, y])
        if not visited[y-1][x]:
            sides.append([x,y-1])
    #border
    if x == 0 and y < h - 1 and y > 0: #Left border
        if not visited[y][x+1]:
            sides.append([x+1,y])
        if not visited[y+1][x]:
            sides.append([x,y+1])
        if not visited[y-1][x]:
            sides.append([x,y-1])
    if 0 < x and x < w - 1 and y == 0: #Up border
        if not visited[y+1][x]:
            sides.append([x,y+1])
        if not visited[y][x-1]:
            sides.append([x-1,y])
        if not visited[y][x+1]:
            sides.append([x+1,y])
    if 0 < x and x < w - 1 and y == h - 1: #Down border
        if not visited[y-1][x]:
            sides.append([x, y-1])
        if not visited[y][x-1]:
            sides.append([x-1,y])
        if not visited[y][x+1]:
            sides.append([x+1,y])
    if x == w - 1 and 0 < y and y < h -1: #right border
        if not visited[y][x - 1]:
            sides.append([x - 1, y])
        if not visited[y + 1][x]:
            sides.append([x,y+1])
        if not visited[y-1][x]:
            sides.append([x,y-1])

    for col,row in sides:
        if not visited[row][col]:
            basins[basin_index] += 1
            visited[row][col] = True
            bfs(col, row, basin_index)
        else:
            print(row,col, basin_index)

for row in range(h):
    for col in range(w):
        if not visited[row][col]:
            basins.append(1)
            visited[row][col] = True
            print(data[row][col], end="+")
            bfs(col,row, len(basins) - 1)
        else:
            print(data[row][col], end="-")
    print("")
basins.sort()
res = [0, 0, 0]
for i in range(3):
    res[i] = basins.pop()
    print(res[i])
print(res[0] * res[1] * res[2])
#for v in visited:
#    for c in v:
#        if c:
#            print(1, end='')
#            continue
#        print(".",end='')
#    print("")












