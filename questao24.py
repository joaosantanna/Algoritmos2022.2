
numero = int(input('Informe um numero para buscar seus divisores:'))

print(f'Divisores de {numero}')
for i in range(1,numero):
    if numero % i == 0:
        print(i)



