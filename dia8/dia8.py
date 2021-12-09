file = open("dia8/dia8.txt", "r")
file.close()
file = open("dia8/dia8_t.txt", "r")

lineas = file.readlines()
patrones = []
numeros = []
contador = 0
#patrones conocidos
pc = [6,2,5,5,4,5,6,3,7,6]
k = 0
for linea in lineas:
    linea = linea.strip("\n")
    patrones.append(linea[0:59].strip())
    numeros.append(linea[60:len(linea)].strip())
    print(patrones, numeros)
    k+=1
file.close()

for numero in numeros:
    _nums = numero.split(" ")
    print(_nums)
    for i in _nums:
        s = len(i)
        if s == pc[1] or s == pc[4] or s == pc[7] or s == pc[8]:
            print(i)
            contador += 1

print(contador)








