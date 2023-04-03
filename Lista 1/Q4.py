
num = '0123456789'
num = list(num)
while True:
    nome = input('Digite seu nome:')
    tem_numero = False
    for n in num:
        if nome.count(n) != 0:
            print('erro nao aceito nomes com numeros')
            print('Tente novamente')
            tem_numero = True
            break
    if not tem_numero:
        break


print(f'Bom dia {nome}')