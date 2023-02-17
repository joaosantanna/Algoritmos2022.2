
print('Detector de Palindromos')
frase = input('Informe uma frase ou palavra:')

frase = frase.lower()

frase_original = list(frase)
frase_teste = frase_original.copy()
frase_teste.reverse()


eh_palindromo = True

for letra in frase_original:
    if letra ==' ':
        frase_original.remove(letra)

for letra in frase_teste:
    if letra == ' ':
        frase_teste.remove(letra)


for p,v in enumerate(frase_original):
    if v != frase_teste[p]:
        eh_palindromo = False


if eh_palindromo:
    print(f' A frase {frase} é um palindromo')
else:
    print(f' A frase {frase} não é um palindromo')
