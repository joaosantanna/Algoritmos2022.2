def numero_primo(numero):
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True

def lista_proximos_10_primos(numero):
    numero_primos = 0
    while numero_primos < 10:
        if numero_primo(numero) :
            print(numero)
            numero_primos += 1
        numero += 1

# incia a rodar nessa linha
n = int(input('Informe o valor de inicio:'))
lista_proximos_10_primos(n)