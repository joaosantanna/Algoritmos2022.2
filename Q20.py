peso = float(input('informe o seu peso:'))
altura = float(input('informe sua altura:'))

imc = peso/(altura**2)

print(f'IMC = {imc:.2f}')

if imc < 20 :
    print('Abaixo do peso ideal')
elif imc >= 20 and imc <= 25:
    print('peso ideal')
else:
    print('sobrepeso')

