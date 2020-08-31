#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://plotly.com/python/creating-and-updating-figures/
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# df = px.data.iris() # iris is a pandas DataFrame
# fig = px.scatter(df, x="sepal_width", y="sepal_length")
# url = 'https://raw.githubusercontent.com/htsong/AppliedDataScience/master/datasets/dataset_wine.csv'


# 用Dash做个WEB应用
app = dash.Dash(
    __name__,
    requests_pathname_prefix='/show_kline/'    
)
app.layout = html.Div([
    dcc.Graph(id='live-update-graph'),
    html.Button('refresh', id='fig-refresh', n_clicks=0)
])

@app.callback(dash.dependencies.Output('live-update-graph', 'figure'),
              dash.dependencies.Input('fig-refresh', 'n_clicks'))
def update_output(n_clicks):
    print('update_output({})'.format('None' if n_clicks==None else n_clicks))
    url = 'http://localhost:8050/get_kline/'
    df = pd.read_csv(url) 
    print(df.shape)
    fig = px.scatter(df, x='ma20', y='close')  #x='alcohol', y='ash')  #y='target' 
    return fig

'''
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
'''
