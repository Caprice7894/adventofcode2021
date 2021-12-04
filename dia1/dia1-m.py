#! /bin/python3

archivo = open("input.txt","r")
lines = archivo.readlines()
_lines = []
for line in lines:
    _lines.append(int(line))
lines = _lines
_lines = []

increases = 0
prevGroup = 0
for i in range(len(lines) - 2):
    group = lines[i] + lines[i+1] + lines[i+2]
    if i == 1:
        prevGroup = group
    if group > prevGroup:
        increases += 1
    print(group)
    prevGroup = group
print(increases)

