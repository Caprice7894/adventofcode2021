class Fish:
    def __init__(self, daysLeft = 8):
        self.daysLeft = daysLeft
        self.justBirth = True
        if daysLeft < 8:
            self.justBirth = False

    def gaveBirth(self):
        self.daysLeft = 6
        return Fish()

    def grow(self):
        if not self.justBirth:
            self.daysLeft -= 1
        else:
            self.justBirth = False
        if self.daysLeft < 0:
            self.daysLeft = 6
            return self.gaveBirth()
        return 0


archivo = open("dia6/dia6.txt")
inp = archivo.readline()
test = "3,4,3,1,2"
test = test.split(",")
#test = inp.split(",")
count = 0
fishes = []
for i in test:
    fishes.append(Fish(int(i)))
    count += 1

for day in range(80):
    for fish in fishes:
        x = fish.grow()
        if x != 0:
            fishes.append(x)
            count += 1

print(count)
