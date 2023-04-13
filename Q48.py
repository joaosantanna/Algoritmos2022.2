from random import randint

numeros =[]

for i in range(10):
    numeros.append(randint(1,100)/10)

print(numeros)

media = 0
soma = 0
for n in numeros:
    soma = soma + n

media = soma/10

print(f' A media = {media:.4f}')

media = sum(numeros)/10
print(f' A media = {media:.4f}')
