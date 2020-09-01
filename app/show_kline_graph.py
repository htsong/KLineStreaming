#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://plotly.com/python/creating-and-updating-figures/
import math
import random
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


def serve_layout():    
    pg = html.Div([
        html.Div([
            dcc.Input(id='time_offset', type='number', placeholder='0'),        
            html.Button('refresh', id='fig-refresh', n_clicks=0)
        ]),
        dcc.Graph(id='live-update-graph'),
        html.Div(id='live-update-text')
    ])        
    return pg
# will get computed everytime you refresh the page, refer to: https://dash.plotly.com/live-updates
app.layout = serve_layout  


@app.callback(dash.dependencies.Output('live-update-graph', 'figure'),
              dash.dependencies.Input('fig-refresh', 'n_clicks'),
               dash.dependencies.Input('time_offset', 'value'))
def load_data(n_clicks, time_off):
    # print('btn clicked {}'.format(n_clicks))
    url = 'http://localhost:8050/get_kline/'
    df = pd.read_csv(url)     # print(df.shape)
    if time_off != None:
        df = df[:time_off]    # 如果时间偏移量不为0，就只取由偏移量指定的前半段数据
    
    fig = px.scatter(df, x='ma20', y='close')  #x='alcohol', y='ash')  #y='target'     
    return fig


'''
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
'''
