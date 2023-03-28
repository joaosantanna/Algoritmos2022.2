import pickle

alunos =[]

print(alunos)

with open('banana.bin','rb') as arq:
    alunos = pickle.load(arq)

print(alunos)
