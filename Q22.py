
n = int(input('Informe o numero para o fatorial:'))
fat1 = 1
fat2 = 1

for i in range(n,1,-1):
    fat1 = fat1 * i

print(f'fatorial de {n} = {fat1}')

for i in range(2, n+1):
    fat2 = fat2 * i
print(f'fatorial de {n} = {fat2}')