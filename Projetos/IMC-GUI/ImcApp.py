import PySimpleGUI as sg
from funcaoApp import calculo_imc

sg.theme('DarkBlue10')

desenho =[
    [sg.Text('Peso:'), sg.InputText(size=(10, 1), key='-PESO-')],
    [sg.Text('Altura:'), sg.InputText(size=(10, 1), key='-ALTURA-')],
    [sg.Button('Calcular IMC'),sg.Text(key='-SAIDA-')],
    [sg.Button('sair',size=(10,))]
]


janela = sg.Window('Calculadora de IMC ', layout=desenho ,
                   font=('Helvetica',12), size=(350, 150))

while True:
    evento, valores = janela.Read()

    if evento in ('sair',sg.WIN_CLOSED):
        break
    if evento == 'Calcular IMC':
        try:
            peso = float(valores['-PESO-'])
            altura = float(valores['-ALTURA-'])
            resultado = calculo_imc(peso,altura)
            janela['-SAIDA-'].update(resultado)
        except Exception as e:
            print(e)


janela.close()