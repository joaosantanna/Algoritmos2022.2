
def calcular_primos(inicio, fim ):
    lista_primos =[]
    for n in range(inicio, fim + 1):
        eh_primo = True
        for i in range(n - 1, 1, -1):
            if n % i == 0:
                eh_primo = False
                break
        if eh_primo:
            lista_primos.append(n)
    return lista_primos








