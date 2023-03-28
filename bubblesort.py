from random import randint
n = []

for i in range(50):
    n.append(randint(-10,100))

for a in range(len(n)):
    for b in range(len(n)):
        if n[a] < n[b]:
            n[a],n[b] = n[b],n[a]

print(n)
