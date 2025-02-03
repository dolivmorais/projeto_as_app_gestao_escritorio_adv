import dash
import plotly.express as px
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

from app import app


# ========= Layout ========= #
layout = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle("Adicione um Advogado")),
    dbc.ModalBody([
        dbc.Row([
            dbc.Col([
                dbc.Label("OAB"),
                dbc.Input(id="adv_oab",placeholder="Apenas números, referente ao OAB" ,type="number")
            ],sm=12,md=6),
            dbc.Col([
                dbc.Label("CPF"),
                dbc.Input(id="adv_cpf",placeholder="Apenas números, referente ao CPF" ,type="number")
            ],sm=12,md=6),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Label("Nome"),
                dbc.Input(id="adv_nome",placeholder="Nome Completo do advogado" ,type="text")
            ]),
        ]),
        html.H5(id="div_erro2")        
    ]),
    dbc.ModalFooter([
        dbc.Button("Cancelar", id="cancel_button_novo_advogado", color='danger'),
        dbc.Button("Salvar", id="save_button_novo_advogado", color='success')
    ])
], id='modal_new_lawyer', size='lg', is_open=False)



# ======= Callbacks ======== #
@app.callback(
    Output('store_adv', 'data'),
    Output('div_erro2', 'children'),
    Output('div_erro2', 'style'),
    Input('save_button_novo_advogado', 'n_clicks'),
    State('store_adv', 'data'),
    State('adv_nome', 'value'),
    State('adv_oab', 'value'),
    State('adv_cpf', 'value')
)
def novo_adv(n_clicks, data_set, nome, oab, cpf):
    erro = []
    style = {}

    # Se store_adv for None, inicializa como lista vazia
    if data_set is None:
        data_set = []

    df_adv = pd.DataFrame(data_set)

    if n_clicks:
        # Verifica se todos os campos foram preenchidos
        if None in [nome, oab, cpf]:
            return data_set, ["Preencha todos os campos"], {'margin-bottom': '10px', 'color': 'red'}

        # Verifica se 'OAB' e 'CPF' já existem na tabela
        if 'OAB' in df_adv.columns and oab in df_adv['OAB'].values:
            return data_set, ["OAB já cadastrado"], {'margin-bottom': '10px', 'color': 'red'}
        
        if 'CPF' in df_adv.columns and cpf in df_adv['CPF'].values:
            return data_set, ["CPF já cadastrado"], {'margin-bottom': '10px', 'color': 'red'}

        # Adiciona novo advogado ao DataFrame
        novo_advogado = pd.DataFrame([[nome, oab, cpf]], columns=['Nome', 'OAB', 'CPF'])
        df_adv = pd.concat([df_adv, novo_advogado], ignore_index=True)

        # Converte para dicionário no formato correto
        dataset = df_adv.to_dict(orient='records')

        # Depuração: printa os dados armazenados
        print("Dados armazenados:", dataset)

        return dataset, ["Cadastro realizado com sucesso"], {'margin-bottom': '10px', 'color': 'green'}

    return data_set, erro, style
