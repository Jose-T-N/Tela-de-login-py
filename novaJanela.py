from PySimpleGUI import PySimpleGUI as sg;


def nova_janela():
    sg.theme('Reddit')
    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Column([[sg.Text('Bém Víndo...')]],
                              element_justification='c'), sg.Push()],
        [sg.VPush()]
    ]
    janela = sg.Window('Aplicativo Desktop', layout, size=(500, 500));

    while True:
        eventos, valores = janela.read();
        if eventos == sg.WIN_CLOSED:
            break;
