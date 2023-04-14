import PySimpleGUI as sg
from funcoesApp import calcular_primos

desenho = [
    [sg.Text('Inicio:'), sg.InputText(size=(10,1), key='-INICIO-')],
    [sg.Text('Fim:'), sg.InputText(size=(10,1), key='-FIM-')],
    [sg.Button('Calcular primos'), sg.Button('sair')],
    [sg.Multiline(size=(100,20),key='-SAIDA-')]
]

janela = sg.Window('Calcula Primos App', layout=desenho ,
                   font=('Helvetica',12), size=(300, 200))

while True:
    evento, valores = janela.Read()

    if evento in ('sair',sg.WIN_CLOSED):
        break
    if evento == 'Calcular primos':
        try:
            inicio = int(valores['-INICIO-'])
            fim = int(valores['-FIM-'])
            resultado = calcular_primos(inicio, fim)
            texto = ''
            for numero in resultado:
                texto += str(numero) + '\n'
            janela['-SAIDA-'].update(texto)
            janela['-INICIO-'].update('')
            janela['-FIM-'].update('')
        except Exception as e:
            print(e)
janela.close()