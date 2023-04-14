print('Fichas de alunos')
nome = input('Informe o nome do aluno:')
idade = int(input('Informe a idade do aluno:'))
n1 = float(input('nota1:'))
n2 = float(input('nota2:'))
n3 = float(input('nota3:'))
n4 = float(input('nota4:'))
notas = [n1,n2,n3,n4]


ficha_aluno = {'nome':nome, 'idade':idade , 'notas':notas}

media = sum(ficha_aluno['notas'])/4
for c , v in ficha_aluno.items():
    print(f'{c} = {v}')
print(f'Media do aluno = {media:.2f}')


