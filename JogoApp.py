import PySimpleGUI as sg
from random import  randint

sg.theme('DarkAmber')
segredo = randint(1,100)
tentativa = 0
desenho =[
    [sg.InputText(key='-ENTRADA-',size=(10,2)), sg.Button('Chutar')],
    [sg.Text('', key='-DICA-')],
    [sg.Button('Novo Jogo'), sg.Button('sair')]
]

janela = sg.Window('Jogo adivinhe numero',
                   font='Arial 18',
                   size=(400,200) ,
                   layout=desenho)

while True:
    evento , valor =janela.read()
    if evento == 'sair' or evento == sg.WIN_CLOSED:
        break
    if evento == 'Novo Jogo':
        janela['-ENTRADA-'].update('')
        segredo = randint(1,100)
        tentativa = 0
        janela['-DICA-'].update('NOVO JOGO !!!')


    if evento == 'Chutar':
        numero = int(valor['-ENTRADA-'])
        if numero == segredo:
            sg.popup(f'Acertou mizeravi \n Tentativas ={tentativa}',
                     font='Arial 18')
        elif segredo > numero:
            tentativa += 1
            janela['-DICA-'].update(f'O numero é maior que {numero}')
        else:
            tentativa += 1
            janela['-DICA-'].update(f'O numero é menor que {numero}')





