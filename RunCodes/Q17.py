print('Digite o numero correspondente ao mes:')
mes = int(input())

nomes_mes = ['Janeiro', 'Fevereiro', 'Março','Abril','Maio','Junho',
             'Julho','Agosto','Setembro', 'Outubro', 'Novembro', 'Dezembro']
if mes < 1 or mes > 12:
    print('mes invalido')
else:
    ajuste = mes - 1
    print(f'mes {mes} corresponde ao mes de {nomes_mes[ajuste]}')
