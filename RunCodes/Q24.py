print('Digite o numero:')
numero = int(input())

num_divisores = 0
for i in range(numero - 1 , 0, -1):
    if numero % i == 0:
        num_divisores +=1
        print(f'{i} é divisor de {numero}')
print(f'numero {numero} possui {num_divisores} divisores')