def calculo_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 20:
        return f'Abaixo do peso ideal - IMC = {imc:.2f}'
    elif imc >= 20 and imc <= 25:
        return f'peso ideal - IMC = {imc:.2f}'
    else:
        return f'sobrepeso - IMC = {imc:.2f}'
