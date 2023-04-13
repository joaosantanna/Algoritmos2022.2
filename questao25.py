soma = 0
for i in range(100,201):
    if i % 7 == 0:
        print(i)
        soma += i   #soma = soma + i

print(f'soma dos multiplos de 7 entre 100 e 200 = {soma}')