def signo(dia, mes):
    if mes == 1:
        if dia <= 20:
            return 'Capricornio'
        else:
            return 'Aquario'
    if mes == 2:
        if dia <= 19:
            return 'Aquario'
        else:
            return 'Peixes'

    if mes == 3:
        if dia <= 20:
            return 'Peixes'
        else:
            return 'Aries'

    if mes == 4:
        if dia <= 20:
            return 'Aries'
        else:
            return 'Touro'
    if mes == 5:
        if dia <= 20:
            return 'Touro'
        else:
            return 'Gemeos'
    if mes == 6:
        if dia <= 20:
            return 'Gemeos'
        else:
            return 'Cancer'

    if mes == 7:
        if dia <= 21:
            return 'Cancer'
        else:
            return 'Leao'

    if mes == 8:
        if dia <= 22:
            return 'Leao'
        else:
            return 'Virgem'

    if mes == 9:
        if dia <= 22:
            return 'Virgem'
        else:
            return 'Libra'

    if mes == 10:
        if dia <= 22:
            return 'Libra'
        else:
            return 'Escorpiao'

    if mes == 11:
        if dia <= 21:
            return 'Escorpiao'
        else:
            return 'Sagitario'

    if mes == 12:
        if dia <= 21:
            return 'Sagitario'
        else:
            return 'Capricornio'

def textoSigno(signo):
    if signo == 'Touro':
        return '''
        TOURO - Momento de perdas, rupturas e desilusões. 
        Quebra de orgulho, quebra de vaidade para que você 
        se redirecione. Não olhe para o passado nem 
        permaneça parado no que já se foi. 
        Promova o autoconhecimento e encontre caminhos mais 
        seguros para caminhar. 
        '''
    elif signo == 'Libra':
        return '''
        LIBRA - Transformação, abandone aquilo que não tem mais 
        sentido em continuar em sua vida e aceite a mudança. 
        Abandone aquilo que não faz mais parte na sua vida sejam 
        relações, pessoas e situações. Vire páginas, coloque um
        ponto final e encerre ciclos. 
        '''