inputFile = open("dia2/dia2.txt", "r")
inputLines = inputFile.readlines()

x = 0
y = 0
aim = 0
for line in inputLines:
    command = line.split(" ")
    command[1] = int(command[1])
    if "forward" in command[0]:
        x+=command[1]
        y += aim * command[1]
    
    if "down" in command[0]:
        #y += command[1]
        aim += command[1]
    
    if "up" in command[0]:
        #y -= command[1]
        aim -= command[1]
    
    print (command, x, y, aim)
print(x, y, x*y)
