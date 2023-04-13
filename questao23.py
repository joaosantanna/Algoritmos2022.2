
while True:
    numero = int(input('Tabuada :'))

    if numero < 1 or numero > 10:
        print('Numero nao pode ser usado')
        print('Digite um numero entre 1 e 10')
        print('Tente novamente')
    else:
        break

print(f'Tabuada de {numero}')

for i in range(1,11):
    print(f'{numero} x {i} = {numero * i}')



soma = 0
i = 100 # inicializacao da variavel de controle
while i <= 200: # condicao de parada
    soma += i # soma = soma + i
    i += 1 # incremento ---- i = i + 1
print(f'Soma = {soma}')


soma = 0
for i in range(100,201):
    soma += i
print(f'Soma = {soma}')
