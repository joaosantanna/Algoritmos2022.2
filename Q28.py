from random import randint
# metodo tradicional - processar os dados enquanto sao gerados
maior_numero = -1001
menor_numero = 1001
for i in range(50):
    n = randint(-1000, 1000)
    print(n)
    if n > maior_numero:
        maior_numero = n
    if n < menor_numero:
        menor_numero = n

print(f'Maior numero = {maior_numero}')
print(f'Menor numero = {menor_numero}')
