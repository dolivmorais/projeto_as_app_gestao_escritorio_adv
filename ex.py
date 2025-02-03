import dash
from dash import html, dcc
from dash.dependencies import Input, Output

# Inicializa a aplicação Dash
app = dash.Dash(__name__)

# Layout da aplicação
app.layout = html.Div([
    html.H1("Exemplo de children no Dash"),
    html.Button("Clique aqui", id="botao", n_clicks=0),
    html.Div(id="saida", children="Texto inicial")  # Div que será atualizada
])

# Callback para atualizar o texto dentro do Div
@app.callback(
    Output("saida", "children"),  # Atualiza o children do componente 'saida'
    Input("botao", "n_clicks")    # Dispara o callback quando o botão é clicado
)
def atualizar_texto(n):
    return f"O botão foi clicado {n} vezes"

# Roda o aplicativo
if __name__ == "__main__":
    app.run_server(debug=True)
