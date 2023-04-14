import PySimpleGUI as sg
from funcoesApp import fibonacci

desenho =[
    [sg.Text('Calculo de termos da serie de Fibonacci')],
    [sg.Text('numero de termos:'), sg.InputText(size=(10, 1), key='-NUMERO-')],
    [sg.Button('Calcular'), sg.Button('sair',size=(10,))],
    [sg.Multiline(key='-SAIDA-', size=(200,20))]
]

janela = sg.Window('Fibonnaci ', layout=desenho ,
                   font=('Helvetica',12), size=(350, 300))

while True:
    evento, valores = janela.Read()

    if evento in ('sair',sg.WIN_CLOSED):
        break
    if evento == 'Calcular':
        try:
            numero_termos = int(valores['-NUMERO-'])
            resultado = fibonacci(numero_termos)
            texto = ''
            for numero in resultado:
                texto += str(numero) + '\n'
            janela['-SAIDA-'].update(texto)
        except Exception as e:
            print(e)
