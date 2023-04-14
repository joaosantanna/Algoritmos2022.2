from random import randint

numeros =[]

for i in range(100):
    numeros.append(randint(1,200))

par = []
impar = []

for n in numeros:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(f'lista de par = {par}')
print(f'lista de impar = {impar}')
print(f'Soma de todos os numeros {sum(numeros)}')
media = sum(numeros)/100
print(f'Media = {media:.2f}')