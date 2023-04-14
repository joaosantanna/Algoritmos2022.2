import time

print('Lista de numeros primos de 100 a 200')
soma = 0
inicio = time.time()
for n in range(100,201):
    eh_primo = True
    for i in range(n-1, 1, -1): 
        if n % i == 0:
            eh_primo = False
            break
    if eh_primo:
        soma += n
        print(n)
fim = time.time()
print(f'A soma dos primos = {soma}')
print(f'Tempo de processamento {fim - inicio}')
