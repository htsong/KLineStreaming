#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# https://plotly.com/python-api-reference/plotly.graph_objects.html
# https://plotly.com/python-api-reference/
#

import math
import random
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output


# 用全局变量存储绘图数据，实现动态更新。
# 但多个用户登陆看到的内容是相同的，这种行为对于多用户的WEB应用来说是错误的。
x=[0, 1, 2, 3, 4, 5, 6, 7, 8]
y=[0, 1, 2, 3, 4, 5, 6, 7, 8]


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(
    html.Div([
        html.H4('Line Live Update'),
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
    ])
)

# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    global x,y
    print(x, y)
    x.append(x[-1] + 1)
    y.append(max(y[-1],1) * random.uniform(0.9, 1.1))    
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y))
    
    # refer to: https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.html#plotly.graph_objects.layout.XAxis
    # One of the following enumeration values:[‘-‘, ‘linear’, ‘log’, ‘date’, ‘category’, ‘multicategory’] 
    # fig.update_layout(xaxis_type="linear", yaxis_type="log", title='对数曲线')    
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
