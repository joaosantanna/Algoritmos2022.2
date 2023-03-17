print('Informe o dia e o mes do seu nascimento')
dia = int(input('Dia:'))
mes = int(input('Mes:'))
if mes == 1:
    if dia <= 20:
        print('Capricornio')
    else:
        print('Aquario')
if mes == 2:
    if dia <= 19:
        print('Aquario')
    else:
        print('Peixes')

if mes == 3:
    if dia <= 20:
        print('Peixes')
    else:
        print('Aries')

if mes == 4:
    if dia <= 20:
        print('Aries')
    else:
        print('Touro')
if mes == 5:
    if dia <= 20:
        print('Touro')
    else:
        print('Gemeos')
if mes == 6:
    if dia <= 20:
        print('Gemeos')
    else:
        print('Cancer')

if mes == 7:
    if dia <= 21:
        print('Cancer')
    else:
        print('Leao')

if mes == 8:
    if dia <= 22:
        print('Leao')
    else:
        print('Virgem')

if mes == 9:
    if dia <= 22:
        print('Virgem')
    else:
        print('Libra')

if mes == 10:
    if dia <= 22:
        print('Libra')
    else:
        print('Escorpiao')

if mes == 11:
    if dia <= 21:
        print('Escorpiao')
    else:
        print('Sagitario')

if mes == 12:
    if dia <= 21:
        print('Sagitario')
    else:
        print('Capricornio')
