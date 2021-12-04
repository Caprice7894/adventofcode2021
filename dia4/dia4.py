#! /bin/python3
archivo = open("dia4/dia4.txt", "r")
lines = []
line = archivo.readline()
while(line):
    lines.append(line.rstrip("\n"))
    line = archivo.readline()
print(lines)
