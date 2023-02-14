"""
nome
email
celular
data aniversario
endereco
disciplina

CRUD - Create, Read, Update, Delete

input/output
tipos basicos de dados
if else elif
while / for
listas
"""
agenda=[
    ['Pedro', 'pedro23@hotmail.com', '9800-7654','20/01','Joao Paulo II, 234',
     'calculo'],
    ['Ana Maria', 'aninha@gmail.com', '9812-5684','18/06','Perimetral n 654',
     'Algoritmos e programação']
]

while True:
    print("""
                Sistema de cadastro de alunos
                0 - sair 
                1 - novo aluno
                2 - listar alunos
                3 - ler dados de um aluno
                4 - atualizar dados de aluno
                5 - apagar aluno
    """)
    op = int(input('>'))
    if op == 0 :
        print('Ate logo!!!')
        break
    elif op == 1:
        # novo aluno
        nome = input('Nome:')
        email = input('Email:')
        telefone = input('Telefone:')
        data_nascimento = input('Data de nascimento:')
        endereco = input('Endereço:')
        disciplina = input('Disciplina:')
        aluno = [nome,email,telefone,data_nascimento,endereco,disciplina]
        agenda.append(aluno)
    elif op == 2:
        for contato in agenda:
            print(contato[0])

    elif op == 3:
        nome = input('Informe o nome que vc procura:')
        achei = False
        for contato in agenda:
            if nome.lower() == contato[0].lower():
                achei = True
                print(f'Nome : {contato[0]}')
                print(f'Email:{contato[1]}')
                print(f'Telefone:{contato[2]}')
                print(f'Data de nascimento:{contato[3]}')
                print(f'Endereço:{contato[4]}')
                print(f'Disciplina:{contato[5]}')
        if achei == False:
            print('Nao achei o contato')

    elif op == 5:
        # apagar aluno
        nome = input('Informe o nome que vc quer apagar:')
        achei = False
        for contato in agenda:
            if nome.lower() == contato[0].lower():
                achei = True
                agenda.remove(contato)
                print(f'Contato apagado = {contato[0]}')
        if achei == False:
            print('Nao achei o contato para apagar')

    elif op == 4:
        nome = input('Informe o nome que vc quer atualizar os dados:')
        achei = False
        for contato in agenda:
            if nome.lower() == contato[0].lower():
                achei = True
                valor_original = contato
                break # quebra o laco for
        if achei == False:
            print('Nao achei o contato para apagar')
        else:
            contato_atualizado = valor_original
            while True:
                print(f'>>>{valor_original}')
                print('''
                        Alteracao de dados de aluno
                        0 - sair
                        1 - nome
                        2 - email
                        3 - telefone
                        4 - data nascimento
                        5 - endereco
                        6 - disciplina
                ''')
                op2 = int(input('>'))
                if op2 == 0 :
                    break
                elif op2 == 1:
                    print(f'Nome: {valor_original[0]}')
                    nome = input('Nome atualizado:')
                    contato_atualizado[0] = nome
                elif op2 == 2:
                    print(f'Email: {valor_original[1]}')
                    email = input('Email atualizado:')
                    contato_atualizado[1] = email
                elif op2 == 3:
                    print(f'Telefone: {valor_original[2]}')
                    telefone = input('Telefone atualizado:')
                    contato_atualizado[2] = telefone
                elif op2 == 4:
                    print(f'Data de Nascimento: {valor_original[3]}')
                    data = input('Data atualizado:')
                    contato_atualizado[3] = data
                elif op2 == 5:
                    print(f'Endereço: {valor_original[4]}')
                    endereco = input('Endereço atualizado:')
                    contato_atualizado[4] = endereco
                elif op2 == 6:
                    print(f'Disciplina: {valor_original[5]}')
                    disciplina = input('Disciplina atualizada:')
                    contato_atualizado[5] = disciplina
            # ao sair do meu
            agenda.remove(valor_original)# apaga registro antigo
            agenda.append(contato_atualizado) # adiciona novo

    else:
        print('Comando não cadastrado')



