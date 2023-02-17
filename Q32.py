print('Lista de numeros primos de 100 a 200')
soma = 0
for n in range(100,201):
    eh_primo = True
    for i in range(n-1, 1, -1):
        if n % i == 0:
            eh_primo = False
            break
    if eh_primo:
        soma += n
        print(n)
print(f'A soma dos primos = {soma}')

