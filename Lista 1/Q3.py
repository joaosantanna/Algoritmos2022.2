frase = input('Digite uma frase:')

vogais = 'aeiouAEIOU'
vogais = list(vogais)
quantidade_vogais = 0
for v in vogais:
    quantidade_vogais += frase.count(v)

print(f'Quantidade de vogais = {quantidade_vogais}')