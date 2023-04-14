def fibonacci(numero_termos):
    if numero_termos == 1:
        termos = [1]
        return termos
    elif numero_termos == 2:
        termos = [1, 1]
        return termos
    else:
        termos = [1, 1]
        contador = 2
        T1 = 1
        T2 = 1
        while contador < numero_termos:
            T3 = T1 + T2
            termos.append(T3)
            T1, T2 = T2, T3
            contador += 1

        return termos
