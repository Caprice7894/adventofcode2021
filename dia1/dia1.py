#! /bin/python3

archivo = open("input.txt","r")
lines = archivo.readlines()

increases = 0
prevScan = int(lines[0])
debug = 0
for scan in lines:
    scan = int(scan)
    if scan > prevScan:
        increases += 1
    prevScan = scan
print(increases)
