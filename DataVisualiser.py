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
    html.H1(children='Sales Data about Pink Morsels'),
    html.Div(children='''
        following line chart shows the sales is higher after the Pink Morsel price increase on the 15th of January 2021, select to see detail date
    '''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
