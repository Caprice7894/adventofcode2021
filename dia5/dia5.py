#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time

archivo = open("dia5/dia5.txt")
lines = []
for line in archivo:
    lines.append(line.rstrip("\n"))
start = []
end = []
class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
    def __add__(self, point):
        x = self.x + point.x
        y = self.y + point.y
        return Point(x,y)
    
    def __sub__(self, point):
        x = self.x - point.x
        y = self.y - point.y
        return Point(x,y)
    
    def __repr__(self):
        return "x: %s, y: %s" % (self.x, self.y)
    def __str__(self):
        return "x: %s, y: %s" % (self.x, self.y)

for line in lines:
    item = line.split(" -> ")
    s = item[0].split(",")
    e = item[1].split(",")
    start.append(Point(s[0],s[1]))
    end.append(Point(e[0],e[1]))

fieldA = [[0 for i in range(1000)] for i in range(1000)]
def print_field(field):
    count = 0
    for row in field:
        for col in row:
            print(col,end=' ')
            if col > 1:
                count += 1
        print("\n", end='')
    print(count)
    time.sleep(0.5)

def mark_point(point):
    fieldA[point.y][point.x] += 1

def move_point(a, b, eje='y'):
    a = b - a
    p = Point(0,0)
    if 'x' in eje:
        if a.x > 0:
            p.x = 1
        elif a.x < 0:
            p.x = -1
    else:
        if a.y > 0:
            p.y = 1
        elif a.y < 0:
            p.y = -1

    return p

for i in range(len(start)):
    if not (start[i].x != end[i].x and start[i].y != end[i].y):
        mark_point(start[i])
    moved = False
    while(start[i].x != end[i].x and start[i].y == end[i].y):
        start[i] = move_point(start[i],end[i], 'x') + start[i]
        mark_point(start[i])
        moved = True

    while(start[i].y != end[i].y and start[i].x == end[i].x and not moved):
        start[i] = move_point(start[i],end[i]) + start[i]
        mark_point(start[i])

print_field(fieldA)
