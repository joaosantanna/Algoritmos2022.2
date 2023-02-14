print('Informe a data do seu nascimento')
dia = int(input('dia:'))
mes = int(input('mes:'))
ano = int(input('ano:'))

dia_atual = 13
mes_atual = 2
idade = 2023 - ano

if mes > mes_atual: # seu niver ainda nao chegou
    idade = 2023 - ano - 1
elif mes < mes_atual: # seu nive ja passou
        idade = 2023 - ano
else: # mes igual ao mes atual
    if dia > dia_atual: # o dia do aniversario ainda nao chegou
        idade = 2023 - ano - 1
    if dia <= dia_atual: # o dia do aniversario já passou ou é hoje !
        idade = 2023 - ano


print(f'Você tem {idade} anos de idade')

