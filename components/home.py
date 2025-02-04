import dash
from dash import html, dcc, callback_context
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

from dash import dash_table
from dash.dash_table.Format import Group

from app import app
from components import modal_novo_processo, modal_novo_advogado, modal_advogados
from sql_beta import df_proc, df_adv


# ========= Styles ========= #
card_style={'height': '100%', 'margin-botton': '12px'}


# Funções para gerar os Cards =======================
# Checar o DataFrame e gerar os icones


# Card padrão de contagem


# Card qualquer de processo


# ========= Layout ========= #
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H3("ENCONTRE O PROCESSO QUE VOCE PRECISA", style={'text-align': 'left', 'margin-left': '32px'}),
        ])
    ]),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Row([
                                dbc.Col([
                                    html.H3("Nº do Processos")
                                ], sm=12, md=8)
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Input(id='processso_filter', placeholder="Insira ...", type="number")
                                ], sm=12, md=12,lg=8),
                                dbc.Col([
                                    dbc.Button(html.I(className="fa fa-search"), id="pesquisa_num_proc", color='danger')
                                ], sm=12, md=12,lg=4),
                            ],style={'margin-bottom': '32px'}),
                            dbc.Row([
                                dbc.Col([
                                    html.H3("STATUS")
                                ])
                            ],style={'margin-bottom': '32px'}),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Checklist(
                                        options=[
                                            {"label": "Concluidos", "value": 1}, {"label": "Vencidos", "value": 2}],
                                        value=[],
                                        id="switches_input",
                                        switch=True,
                                    ),
                                ])
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    html.H3("INSTÂNCIA")
                                ])
                            ],style={'margin-top': '24px'}),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Checklist(
                                        options=[{"label": "1A Instância", "value": 1}, {"label": "2A Instância", "value": 2}],
                                        value=[1,2],
                                        id="checklist_input",
                                    ),
                                ])
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    html.H3("CPF do cliente")
                                ])
                            ],style={'margin-top': '24px'}),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Button(html.I(className="fa fa-search"), id="pesquisa_cpf", color='light')
                                ],sm=2),
                                dbc.Col([
                                    dbc.Input(id='cpf_filter', placeholder="Insira o CPF ...", type="number")
                                ],sm=10)
                                
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    html.H3("ADVOGADO")
                                ])
                            ],style={'margin-top': '24px'}),
                            dbc.Row([
                                dbc.Col([
                                    dcc.Dropdown(id='advogado_filter', className='dbc',
                                    placeholder="Selecione um ou mais advogados", 
                                    options=[{'label': i, 'value': i} for i in df_adv['Advogado']])
                                ])
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Button("Todos os Processos", id="podos_processos",style={'width': '100%'}, color="dark")
                                ])
                            ],style={'margin-top': '24px'})
                        ], style={'margin': '20px'})
                    ])
                ])
            ])
        ],sm=12,md=5,lg=5),
        dbc.Col([
            dbc.Container(
                id='card_generator',fluid=True,style={'whdth': '100%', 'padding': '0px 0px 0px 0px', 'margin': '0px 0px 0px 0px'})
            ],sm=12,md=7,lg=7,style={'padding-left': '0px'})
        ])
], fluid=True,style={'height': '100vh', 'padding': '10px', 'margin': 0, 'padding-left': '0px'})




# ======= Callbacks ======== #
# Callback pra atualizar o dropdown de advogados


# Callback pra atualizar o dropdown de clientes


# Callback pra atualizar o dropdown de processos


# Callback pra gerar o conteudo dos cards

