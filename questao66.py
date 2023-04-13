from random import randint

dados = { 2:0, 3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}

for i in range(1000):
    valor =randint(2,12)
    dados[valor] += 1

for c, v in dados.items():
    print(f'{c} - {(v*100/1000):.2f} %')

