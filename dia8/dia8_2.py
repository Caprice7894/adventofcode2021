from time import sleep

pc = [6,2,5,5,4,5,6,3,7,6]
con = {}
def conocidos(s):
    i = len(s)
    if i == pc[1]:
        con["1"] = s
    elif i == pc[4]:
        con["4"] = s
    elif i == pc[7]:
        con["7"] = s
    elif i == pc[8]:
        con["8"] = s

    if "4" in con and "1" in con:
        _t = []
        for i in range(4):
            if con["4"][i] not in con["1"]:
                _t.append(con["4"][i])
        con["L"] = _t
def numeros_restantes(arr):
    for num in arr:
        if len(con) == 11:
            break
        lnum = len(num)
        if lnum == 5:
            contador = 0
            for i in con["1"]:
                if i in num:
                    contador += 1
            if contador == 2:
                con["3"] = num
                continue
            contador = 0
            for i in con["L"]:
                if i in num:
                    contador += 1
            if contador == 2:
                con["5"] = num
                continue
            con["2"] = num
            continue
        if lnum == 6:
            contador = 0
            for i in con["4"]:
                if i in num:
                    contador += 1
            if contador == 4:
                con["9"] = num
                continue
            contador = 0
            for i in con["L"]:
                if i in num:
                    contador += 1
            if contador == 2:
                con["6"] = num
                continue
            con["0"] = num
            continue


file = open("dia8/dia8.txt", "r")
#file.close()
#file = open("dia8/dia8_t.txt", "r")
lineas = file.readlines()
patrones = []
numeros = []
consArr = []
contador = 0
k = 0
for linea in lineas:
    linea = linea.rstrip("\n")
    patrones.append(linea[0:59].rstrip(" "))
    numeros.append(linea[60:len(linea)].strip())
    k+=1
file.close()
for numero in patrones:
    con = {}
    _nums = numero.split(" ")
    for i in range(len(_nums)):
        _nums[i] = list(_nums[i])
        _nums[i].sort()
    
    for i in _nums:
        conocidos(i)
    numeros_restantes(_nums)
    _con = {}
    for key in con:
        if key == "L":
            continue
        _con["".join(con[key])] = key
    consArr.append(_con)
sumatoria = 0
for i in range(len(patrones)):
    num = numeros[i].split(" ")
    valor = 0
    for j in range(len(num)):
        string = list(num[j])
        string.sort()
        num[j] = "".join(string)
    m = 3
    for j in num:
        valor += int(consArr[i][j]) * (10 **m)
        m -= 1
        print(consArr[i][j], end='')
    print("\n", valor)
    sumatoria += valor
print(sumatoria)




