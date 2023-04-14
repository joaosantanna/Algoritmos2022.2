
def inverter_numero(numero):
    texto = str(numero)
    lista_de_numeros = list(texto)
    lista_de_numeros.reverse()
    numero = ''
    for n in lista_de_numeros:
        numero += n
    numero = int(numero)
    return numero


n = int(input('Qual numero vc quer reverter:'))
r = inverter_numero(n)
print(r)
