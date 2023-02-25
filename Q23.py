# entradas n

while True:
    n = int(input('Informe o valor de n:'))
    if n >= 1 and n <= 10:
        break
    else:
        print('erro só aceito numeros entre 1 e 10')

for i in range(1,11):
    print(f'{n} x {i} = {n*i}')

