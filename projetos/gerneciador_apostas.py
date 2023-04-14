import pickle
from random import randint
apostas =[]

# tentar ler os dados do disco se existirem

try:
    with open('apostas_mega.bin','rb') as arq:
        apostas = pickle.load(arq)
except Exception :
    print('Arquivo não existe')

while True:

    print('''
        Gerenciador de apostas - Mega Sena
        0 - Sair
        1 - Novo jogo
        2 - ver os jogos feitos
        3 - Conferir apostas
        4 - Salvar dados
        5 - apagar jogo
    ''')
    op = int(input('opção:'))

    if op == 0 :
        print('tchau!!')
        break
    if op == 1:
        q = input('Quantos numeros vc quer apostar(6):')
        if q =='':
            q = 6
        else:
            q = int(q)

        if q < 6:
            print('Mega sena aposta minima = 6 numeros')
        else:
            r = input('Vc quer fazer aposta automatica(s)(n)?')
            if r == 's': # aposta automatica
                jogo =[]
                numero_valido = 0
                while numero_valido < q:
                    n = randint(1,60)
                    if n not in jogo:
                        jogo.append(n)
                        numero_valido  += 1
                jogo.sort()
                apostas.append(jogo)
            else: # aposta manual
                jogo = []
                print(f'digite {q} numeros para a sua aposta')
                numero_valido = 0
                while True:
                    n = int(input('>'))
                    if n >= 1 and n <= 60:
                        if n not in jogo:
                            jogo.append(n)
                            numero_valido += 1
                        else:
                            print('Erro - Numero ja existe no jogo')
                    else:
                        print('Erro - Numero fora do range de 1 a 60')
                    if numero_valido == q:
                        break
                jogo.sort()
                apostas.append(jogo)

    if op == 2:
        print('Apostas guardadas no sistema:')
        for p,  jogo in enumerate(apostas):
            print(f'{p+1} - {jogo}')

    if op == 3:
        resultado = []
        print(f'digite os 6 numeros sorteados:')
        for i in range(6):
            n = int(input('>'))
            resultado.append(n)


        # conferir acertos ...
        print(f'Numeros sorteados = {resultado}')
        for jogo in apostas:
            numero_acerto = 0
            for numero in resultado:
                if numero in jogo:
                    numero_acerto += 1
            print(f'{jogo} - numero de acertos = {numero_acerto}')

    if op == 4:
        with open('apostas_mega.bin','wb') as arq:
            pickle.dump(apostas, arq)
        print('Dados salvos com sucesso!!')

    if op == 5 :
        print('Qual jogo vc quer apagar?')
        j = int(input('>'))
        jogo = apostas.pop(j-1)
        print(f'Jogo {jogo} apagado')
