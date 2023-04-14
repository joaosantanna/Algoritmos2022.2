numeros = [1,1]
t1 = 1
t2 = 1
t3 = 0
soma = 0
while t3 <= 1000:
    t3 = t1 + t2
    numeros.append(t3)
    if t3 % 2 == 0:
        print(t3)
        soma += t3
    t1, t2 = t2, t3

print(f' soma dos pares da serie F = {soma}')
print(numeros)
