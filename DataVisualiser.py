# generate a line chart with dash
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

data = pd.read_csv("data/daily_sales_data_output.csv", sep=",")
# show were sales higher before or after the Pink Morsel price increase on the 15th of January 2021

fig = px.line(data, x="date", y="sales", color="region")
fig.update_traces(mode="lines")
app.layout = html.Div(children=[
    html.Div([
        html.H1(children='Sales Data about Pink Morsels'),
        html.Div(children='''
            following line chart shows the sales is higher after the Pink Morsel price increase on the 15th of January 2021, select to see detail date
        ''')
    ], style={'text-align': 'center', 'color': '#5459E3', 'background-color': '#5EE1FD', 'padding-top': '10px', 'padding-bottom': '20px', 'margin-top': '40px'}),

    html.Div([
        dcc.Graph(
            id='example-graph',
            figure=fig
        ),
        ], style={'margin-top': '30px'}),

    html.Div([
        dcc.RadioItems(
            ['north', 'east', 'south', 'west', 'all'],
            'all',
            id='region-selector',
            inline=True
        )
    ], style={'width': '100%', 'display': 'inline-block', 'padding-left': '550px'})
])

@app.callback(
    Output('example-graph', 'figure'),
    Input('region-selector', 'value')
)
def update_graph(region_selector=None):
    if 'all' in region_selector:
        data = pd.read_csv("data/daily_sales_data_output.csv", sep=",")
    else:
        data = pd.read_csv("data/daily_sales_data_output.csv", sep=",")
        data = data[data['region'] == region_selector]
    fig = px.line(data, x="date", y="sales", color="region")
    fig.update_traces(mode="lines")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
