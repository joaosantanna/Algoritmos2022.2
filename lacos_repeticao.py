print('Calculo do Fatorial de n')
tentativa = 0
while True:
    n = int(input('digite o valor de n:'))
    tentativa = tentativa + 1
    if n < 0:
        print('Erro só trabalho com numeros positivos')
        if tentativa > 4:
            print('Tu é burrao, cansei')
            break
    elif n == 0:
        print(f'o fatorial de 0 = 1')
        break
    else:
        fat = 1
        for i in range(1,n+1):
            fat = fat * i
        print(f'o fatorial de {n} = {fat}')
        break



