#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time

archivo = open("dia5/dia5.txt")
w = 0
h = 0
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
    if int(s[0]) > w:
        w =int(s[0])
    if int(e[0]) > w:
        w = int(e[0])
    if int(s[1]) > h:
        h = int(s[1])
    if int(e[1]) > h:
        h = int(e[1])
    end.append(Point(e[0],e[1]))

fieldA = [[0 for i in range(w + 1)] for i in range(h + 1)]
def print_field(field):
    count = 0
    for row in field:
        for col in row:
            if col > 1:
                count += 1
    print(count,end='\n')
#    time.sleep(0.5)

def mark_point(point):
    fieldA[point.y][point.x] += 1

def sign(value):
    if value > 0:
        return 1
    elif value < 0:
        return -1
    return 0

def move_point(a, b, eje='y'):
    a = b - a
    p = Point(0,0)
    if 'x' in eje:
        p.x = sign(a.x)
    elif 'y' in eje:
        p.y = sign(a.y)
    elif 'b' in eje:
        p.x = sign(a.x)
        p.y = sign(a.y)

    return p

for i in range(len(start)):
#    if not (start[i].x != end[i].x and start[i].y != end[i].y):
    mark_point(start[i])
    moved = False
    _start = start[i]
    while(start[i].x != end[i].x and start[i].y == end[i].y):
        start[i] = move_point(start[i],end[i], 'x') + start[i]
        mark_point(start[i])
        moved = True

    while(start[i].y != end[i].y and start[i].x == end[i].x and not moved):
        start[i] = move_point(start[i],end[i]) + start[i]
        mark_point(start[i])
    while(_start.y != end[i].y or _start.x != end[i].x): 
        raice = (end[i].y - _start.y)
        runn = (end[i].x - _start.x)
        if runn != 0:
            m = raice / runn
            if m == 1 or m == -1:
                _start = move_point(_start, end[i],'b') + _start
                mark_point(_start)
            else:
                break
        else:
            break
print_field(fieldA)
