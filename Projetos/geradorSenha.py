from string import ascii_letters, digits
from random import choice
tamanho = int(input('Tamanho da senha:'))

caracteres = ascii_letters + digits + '!#@$*'

# montando a senha
senha = ''
for i in range(tamanho):
    senha += choice(caracteres)

print(f'Senha = {senha}')