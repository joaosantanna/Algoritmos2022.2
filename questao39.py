def numero_primo(numero):
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True

r = numero_primo(39)
print(f'numero 39 é primo = {r}')
