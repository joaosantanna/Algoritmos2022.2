import time
n = int(input('Informe o numero:'))

eh_primo = True
inicio = time.time()
for i in range(2, n):
    if n % i == 0:
        print(i)
        eh_primo = False
        break
fim = time.time()
if eh_primo:
    print(f'Numero {n} é primo')
else:
    print(f'Numero {n} não é primo')
print(f'Tempo de processamento {fim - inicio}')