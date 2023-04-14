from  random import randint

l = []
for i in range(20):
    l.append(randint(1,100))

l.sort()
print(l)