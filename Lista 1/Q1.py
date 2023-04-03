from random import randint

lista = []
for i in range(10):
    lista.append(randint(1,15))

numero = int(input('Digite um numero entre 1 e 15:'))
f = lista.count(numero)
if f == 0:
    print(f'numero {numero} nao existe na lista')
    print(f'Lista = {lista}')
else:
    print(f'Numero presente na lista')
    for p,v in enumerate(lista):
        if v == numero:
            print(f'posicao {p}')
    print(f'Lista = {lista}')
