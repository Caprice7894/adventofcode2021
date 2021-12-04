#! /bin/python3

archivo = open("dia3/dia3_ej.txt","r")
inp = archivo.readlines()
_inp = inp
trues = []
falses = []

for byte in range(len(inp[0]) - 1):
    for line in inp:
        if "1" in line[byte]:
            trues.append(line)
        else:
            falses.append(line)
    if len(trues) > len(falses):
        inp = trues
    elif len(falses) > len(trues):
        inp = falses
    else:
        inp = trues
    if len(inp) == 1:
        break
    trues = []
    falses = []
ox = inp[0]
oxigen = ox
inp = _inp
_inp = 0
for byte in range(len(inp[0]) - 1):
    for line in inp:
        if "1" in line[byte]:
            trues.append(line)
        else:
            falses.append(line)
    if len(trues) > len(falses):
        inp = falses
    elif len(falses) > len(trues):
        inp = trues
    else:
        inp = falses
    if len(inp) == 1:
        break
    trues = []
    falses = []
co = inp[0]
dioxide = co
x = 0
y = 0

for i in range(len(oxigen)):
    byte = len(oxigen) - (i + 2)
    if "1" in oxigen[byte]:
        x+=2**i
    if "1" in dioxide[byte]:
        y+=2**i
print(x*y)
