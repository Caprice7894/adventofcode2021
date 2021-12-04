#! /bin/python3

archivo = open("dia3/dia3_ej.txt","r")
inp = archivo.readlines()

gamma = []
epsilon = []

t_count = 0
f_count = 0

for i in range(len(inp[0]) - 1):
    for j in range(len(inp)):
        if "1" in inp[j][i]:
            t_count += 1
        else:
            f_count += 1
    if t_count > f_count:
        gamma.append("1")
        epsilon.append("0")
    else:
        gamma.append("0")
        epsilon.append("1")
    t_count = 0
    f_count = 0
print(gamma, epsilon)

s = len(gamma)
g = 0
e = 0
for i in range(s):
    print (gamma[(s-1)-i],epsilon[(s - 1) - i])
    _g = int(gamma[(s-1)-i])
    _e = int(epsilon[(s-1)-i])
    
    if _g != 0:
        g += 2 ** i

    if _e != 0:
        e += 2 ** i

print("gamma: ", g, "epsilon: ", e)
print(g*e)
