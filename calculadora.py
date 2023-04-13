from operacoes.operacoes import *

print('Escolha a operacao que vc quer:')
print('''
        1- soma
        2 - subtracao
        3 - multiplicacao
''')

op = int(input('>'))
n1 = float(input('Informe o primeiro valor:'))
n2 = float(input('Informe o segundo valor:'))
if op == 1:
    print(f'soma de {n1} + {n2} = {soma(n1,n2):.2f}')
elif op == 2:
    print(f'subtracao de {n1} - {n2} = {subtracao(n1,n2):.2f}')
elif op == 3:
    print(f'multiplicacao de {n1} x {n2} = {multiplicacao(n1,n2):.2f}')
else:
    print('comando nao cadastrado')

