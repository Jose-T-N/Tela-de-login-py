from PySimpleGUI import PySimpleGUI as sg
from sqlConexao import *
from novaJanela import *

# conexão com o banco
criar_banco();
criar_tabela();

# layout
sg.theme('Reddit');
layout = [
    [sg.Text('usuário'), sg.Input(key='usuario')],
    [sg.Text('senha'), sg.Input(key='senha', password_char='*')],
    [sg.Button('Entrar'), sg.Button('Salvar')],
];
# Janela
janela = sg.Window('Tela de Login', layout);
# ler Eventos
while True:
    eventos, valores = janela.read();
    #fecha janela
    if eventos == sg.WIN_CLOSED:
        break;

    # evento entrar
    if eventos == 'Entrar':
        if len(valores['usuario']) != 0 and len(valores['senha']) != 0:
            # valores do banco de dados
            dados = pesquisa(valores['usuario']);
            if len(dados) != 0:
                # comparando os valores dos inputs com os do banco
                if valores['usuario'] == dados[0][0] and valores['senha'] == str(dados[0][1]):
                    janela.close();
                    nova_janela();
                else:
                    sg.Popup('Senha incorreta');
                    #print('Senha incorreta');
            else:
                sg.Popup('Usuário inexistente');
                #print('Usuário inexistente');
        else:
            sg.Popup('Porfavor preencher todos os dados');
    # evento salvar
    if eventos == 'Salvar':
        if len(valores['usuario']) != 0 and len(valores['senha']) != 0:
            if adicionar_linha(valores['usuario'], valores['senha']):
                sg.Popup('Usuário salvo');
                print(pesquisa(valores['usuario']));
            else:
                sg.Popup(
                    "Já existe um usuário com esse nome. Porfavor escolher outro!");
                #print('Já existe um usuário com esse nome. Porfavor escolher outro!');
        else:
            sg.Popup('Porfavor preencher todos os dados');
