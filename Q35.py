from math import pi
erro = pi - 3
print(f'1 = 3 - erro ={erro}')
soma = 3
n = 2
for i in range(2,16):
    if i % 2 == 0:
        t = 4/(n * (n+1) * (n+2) )
        soma += t
        erro = pi - soma
        print(f'{i} = {soma} - erro ={erro}')
        n += 2
    else:
        t = -4 / (n * (n + 1) * (n + 2))
        soma += t
        erro = pi - soma
        print(f'{i} = {soma} - erro ={erro}')
        n += 2