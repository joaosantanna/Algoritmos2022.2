from random import randint

lista = []
for i in range(20):
    lista.append(randint(1,100))

q_par = 0
q_impar = 0

for n in lista:
    if n % 2 == 0:
        q_par += 1
    else:
        q_impar += 1
print(f'l = {lista}')
print(f'Quantidade de pares = {q_par}')
print(f'Quantidade de impares = {q_impar}')

