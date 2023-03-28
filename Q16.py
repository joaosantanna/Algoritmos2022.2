nome = input('Informe seu nome:')
sexo = int(input('Informe seu sexo 1-masculino 2-feminino:'))

if sexo == 1:
    print(f'Ilustrissimo sr. {nome}')
elif sexo == 2:
    print(f'Ilustrissima srta. {nome}')
else:
    print('Nao entendi ....')
