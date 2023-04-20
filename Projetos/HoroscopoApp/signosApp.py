import PySimpleGUI as sg
from funcaoApp import signo, textoSigno

sg.theme('dark grey 9')
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio',
       'junho', 'julho','agosto','setembro', 'outubro', 'novembro',
       'dezembro']

desenho = [
    [sg.Text('Descubra seu signo do zodiaco', font=('helvetica','28'))],
     [sg.Image(filename='zodiaco.png', size=(200,200))],
    [sg.Text('Dia:'), sg.InputText(key='-DIA-')],
    [sg.Text('Mes:'), sg.Combo(meses, key='-MES-')],
    [sg.Button('Descobrir'),sg.Button('sair')],
    [sg.Multiline(key='-TEXTO-', size=(50,10))]
]

janela = sg.Window('Signo App', layout=desenho, font=('helvetica', 12))

while True:
    evento, valor = janela.Read()

    if evento in ('sair', sg.WIN_CLOSED):
        break
    if evento == 'Descobrir':
        dia = int(valor['-DIA-'])
        mes = valor['-MES-']
        for p, m in enumerate(meses):
            if mes == m:
                mes = p + 1

        resultado = signo(dia,mes)
        janela['-TEXTO-'].update(textoSigno(resultado))


janela.close()