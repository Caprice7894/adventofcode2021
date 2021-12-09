file = open("dia9/dia9.txt", "r")
#file.close()
#file = open("dia9/dia9_t.txt", "r")

data = []
h = 0
for row in file:
    row = list(row.rstrip("\n"))
    _row = [int(x) for x in row]
    data.append(_row)
    h+= 1

file.close()
w = len(data[0])
print(w, h)
#h = len data
low_points = []
for row in range(h):
    col = 0
    print(data[row])
    while col < w:
        d = data[row][col]
        #up left corner
        if row == 0 and col == 0:
            down = data[1][0]
            right = data[0][1]
            if d < down and d < right and (down + right) < 18:
                low_points.append(d)
                print("up left corner = ", d)
        #up right corner
        elif row == 0 and col == w - 1:
            down = data[1][col]
            left = data[0][col - 1]
            if d < left and d < down and (down + left) < 18:
                low_points.append(d)
                print("up right corner = ", d)
        #down left corner
        elif row == h - 1 and col == 0:
            up = data[row - 1][0]
            right = data[row][1]
            if d < up and d < right and (up + right) < 18:
                low_points.append(d)
                print("down left corner = ", d)
        #down right corner
        elif row == h - 1 and col == w - 1:
            up = data[row - 1][col]
            left = data[row][col - 1]
            if d < up and d < left and (up + left) < 18:
                low_points.append(d)
                print("left right corner = ", d)
        #up edge
        elif row == 0 and 0 < col and col < w - 1:
            left = data[row][col - 1]
            down = data[row + 1][col]
            right = data[row][col + 1]
            if d < left and d < down and d < right and (left + down + right) < 27:
                low_points.append(d)
                print("up edge = ", d)
        #left edge
        elif col == 0 and row < h - 1 and row > 0:
            up = data[row - 1][col]
            down = data[row + 1][col]
            right = data[row][col + 1]
            if d < up and d < down and d < right and (up + down + right) < 27:
                low_points.append(d)
                print("left edge = ", d)
        #down edge
        elif row == h - 1 and col > 0 and col < w - 1:
            up = data[row - 1][col]
            right = data[row][col + 1]
            left = data[row][col - 1]
            if d < up and d < right and d < left and (up + right + left) < 27:
                low_points.append(d)
                print("down edge = ", d)
        #right edge
        elif col == w - 1 and row > 0 and row < h - 1:
            up = data[row - 1][col]
            down = data[row + 1][col]
            left = data[row][col - 1]
            if d < up and d < down and d < left and (up + down + left) < 27:
                low_points.append(d)
                print("right edge = ", d)
        #inside items
        elif h - 1 > row and row > 0 and w - 1 > col and col > 0:
            up = data[row - 1][col]
            down = data[row + 1][col]
            left = data[row][col - 1]
            right = data[row][col + 1]
            if d < up and d < down and d < left and d < right and (up + down + left + right) < 36:
                low_points.append(d)
                print("inside items = ", d)
        col += 1
print(sum(low_points))
s = 0
for i in low_points:
    s += i + 1
print(s)
