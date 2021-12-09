from time import sleep
from math import ceil, floor
archivo = open("dia6/dia6.txt")
inp = archivo.readline()
inp = inp.rstrip("\n")
test = "3,4,3,1,2"
test = test.split(",")
test = inp.split(",")

count = 0
fishes = {}

for i in test:
    if i not in fishes:
        fishes[i] = 1
        continue
    fishes[i] += 1

print(fishes)
days = 256
data = [0,0,0,0,0,0,0,0,0]

for fish in fishes:
    data[int(fish)] = fishes[fish]
    print(data)

for day in range(days):
    _data = [0 for i in range(len(data))]
    for d in range(len(data)):
        if d == 0:
            _data[6] += data[0]
            _data[8] += data[0]
        else:
            _data[d - 1] += data[d]
    data = _data
res = 0
for c in data:
    res += c

print(res)
