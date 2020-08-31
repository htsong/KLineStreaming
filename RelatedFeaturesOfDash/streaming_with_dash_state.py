#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# https://plotly.com/python-api-reference/plotly.graph_objects.html
# https://plotly.com/python-api-reference/
#

import math
import random
import json

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State


# 用全局变量存储绘图数据，实现动态更新。
# 但多个用户登陆看到的内容是相同的，这种行为对于多用户的WEB应用来说是错误的。
# refer to: https://dash.plotly.com/sharing-data-between-callbacks
x=[0, 1, 2, 3, 4, 5, 6, 7, 8]
y=[0, 1, 2, 3, 4, 5, 6, 7, 8]


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.Div([
        html.H4('Line Live Update'),
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
        
    ]),
    # Hidden div inside the app that stores the intermediate value
    html.Div(id='intermediate-value', style={'display': 'none'})    
])

# Multiple components can update everytime interval gets fired.  
@app.callback([Output('live-update-graph', 'figure'),
               Output('intermediate-value', 'children')],
              Input('interval-component', 'n_intervals'),
              State('intermediate-value', 'children'))
def update_graph_live(n, txt):
    global x,y
    
    if txt == None:                                                   # TODO: 此处应改为在页面加载时做一次，现在这种做法首次调用会有错误。
        txt = json.dumps(obj = {'x':x, 'y':y})
    #print(x, y, txt)
    
    dt = json.loads(txt)
    dt['x'].append(dt['x'][-1] + 1)
    dt['y'].append(max(dt['y'][-1],1) * random.uniform(0.9, 1.1)) 

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dt['x'], y=dt['y']))
    
    # refer to: https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.html#plotly.graph_objects.layout.XAxis
    # One of the following enumeration values:[‘-‘, ‘linear’, ‘log’, ‘date’, ‘category’, ‘multicategory’] 
    # fig.update_layout(xaxis_type="linear", yaxis_type="log", title='对数曲线')    
    
    return fig, json.dumps(obj = dt)

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
