import plotly
import plotly.express as px
import json
import pandas as pd
import backend.stocks as st
import dash 
import dash_core_components as dcc
import dash_html_components as html



app = dash.Dash(__name__)


fig = st.Stock("AAPL").get_timeseries()


app.layout = html.Div([
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)

