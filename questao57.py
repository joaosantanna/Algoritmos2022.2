from random import randint
aposta =[]

while len(aposta) < 6:
    numero = randint(1,60)
    if numero not in aposta:
        aposta.append(numero)

aposta.sort()
print(aposta)


