alunos =['ana', 'beatriz', 'dudu', 'pedro']

print('cadastre mais 3 alunos')
for i in range(3):
    nome = input('Nome:')
    alunos.append(nome)

with open('banana.txt','w') as arq:
    for nome in alunos:
        arq.write(nome + '\n')
print('Dados salvo com sucesso')