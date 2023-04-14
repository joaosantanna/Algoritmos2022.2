turma =[]
while True:
    print('''
        0 - sair
        1 - cadastrar nome e idade de aluno
        2 - cadastrar notas dos alunos
        3 - imprimir dados da turma
        4 - lista de aprovados
        5 - lista de alunos em recuperacao
        ''')
    op = int(input('Opção :'))

    if op == 0 :
        print('tchau')
        break
    if op == 1:
        nome = input('Informe o nome do aluno:')
        idade = int(input('Informe a idade do aluno:'))
        ficha_aluno = {'nome':nome, 'idade':idade }
        turma.append(ficha_aluno)
    if op == 2:
        print('Informe o nome do alunos para a entrada de notas')
        for aluno in turma:
            print(aluno['nome'])
        nome = input('Nome:')
        print(f'Entre com as 4 notas de {nome}')
        n1 = float(input('nota1:'))
        n2 = float(input('nota2:'))
        n3 = float(input('nota3:'))
        n4 = float(input('nota4:'))
        notas = [n1, n2, n3, n4]
        for ficha in turma:
            if ficha['nome'] == nome:
                ficha['notas'] = notas


    if op == 3:
        for aluno in turma:
            print(aluno)

    if op == 4:
        print('Lista dos aprovados')
        for ficha in turma:
            media = sum(ficha['notas'])/4
            ficha['media'] = media
        for ficha in turma:
            if ficha['media'] >= 6:
                print(f"{ficha['nome']} - {ficha['media']}  ")
    if op == 5:
        print('Lista dos alunos em recuperacao')
        for ficha in turma:
            media = sum(ficha['notas']) / 4
            ficha['media'] = media
        for ficha in turma:
            if ficha['media'] < 6:
                print(f"{ficha['nome']} - {ficha['media']}  ")