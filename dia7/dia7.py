from time import sleep
from math import floor, ceil
file = open("dia8/dia8.txt", "r")
file = file.readline()

def make_int(inpu):
    for i in range(len(inp)):
        inpu[i] = int(inpu[i])
    return inpu

test = "16,1,2,0,4,2,7,1,2,14"
#file = test

inp = file.rstrip().split(",")
inp = make_int(inp)
inp.sort()

arr = []
rep = {}
#fill repeated fields
for i in inp:
    if str(i) not in rep:
        rep[str(i)] = 0
        arr.append(int(i))
    rep[str(i)] += 1


def dif (x1, x2):
    if x1 > x2:
        return x1 - x2
    else:
        return x2 - x1

def sumar_combustible(x, array):
    suma = 0
    for i in range(0, len(array)):
        if x < array[i]:
            n = (array[i] - x)
            s = n * (n + 1) / 2
            r = s * rep[str(array[i])]
            suma += r

        elif array[i] < x:
            n = (x - array[i])
            s = n * (n + 1) / 2
            r = s * rep[str(array[i])]
            suma += r

    return suma

# 0  1  2  3  4  5   6
#[0, 1, 2, 4, 7, 14, 16]
minimo = sumar_combustible(arr[0], arr)

for x in range(arr[0] + 1, arr[len(arr) - 1]):
    res = sumar_combustible(x, arr)
    if res < minimo:
        minimo = res
        continue
print(minimo)







