import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import sqlite3

# import from folders
from app import *
from components import home, sidebar
from sql_beta import df_adv, df_proc

# Criar estrutura para Store intermediária ==============



# =========  Layout  =========== #
app.layout = dbc.Container([
    # Store e Location 
    dcc.Location(id='url'),
    dcc.Store(id='store_intermedio',data={}),
    dcc.Store(id='store_adv',data=df_adv.to_dict()),
    dcc.Store(id='store_proc',data=df_proc.to_dict()),
    html.Div(id='div_fantasma'),

    

    # Layout
    dbc.Row([
        dbc.Col([
            sidebar.layout
        ], md=2, style={'padding': '0px'}),
        dbc.Col([
            dbc.Container(id='page-content', fluid=True, style= {'height': '100vh','width': '100%', 'padding-left': '14px'})
        ],md=10, style={'padding': '0px'})
    ])

], fluid=True)


# ======= Callbacks ======== #
# URL callback to update page content
@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def render_page(pathname):
    if pathname == '/home' or pathname == '/':
        return home.layout
    else:
        return dbc.Jumbotron([
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.Div(f"The pathname {pathname} was not recognised..."),
            html.P(f'O caminho {pathname} não foi reconhecido...'),
            html.P(f'Use NavBar para navegar entre as páginas corretamente...')
        ])

# Dcc.Store back to file
@app.callback(
    Output('div_fantasma', 'children'),
    Input('store_adv', 'data'),
    Input('store_proc', 'data'),)
def update_files(adv_data, procv_data):
    df_adv_aux = pd.DataFrame(adv_data)
    df_proc_aux = pd.DataFrame(procv_data)

    #preencher com codigo sql
    conn = sqlite3.connect('sistema.db')
    df_adv_aux.to_sql('advogados', conn, index=False, if_exists='replace')
    conn.commit()
    df_proc_aux.to_sql('processos', conn, index=False, if_exists='replace')
    conn.commit()

    conn.close()
    return []


if __name__ == '__main__':
    app.run_server(debug=True)
