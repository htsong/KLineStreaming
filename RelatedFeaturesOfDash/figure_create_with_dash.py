
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# https://plotly.com/python-api-reference/plotly.graph_objects.html
# https://plotly.com/python-api-reference/
#

import math
import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objects as go
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[math.exp(k) for k in [0, 1, 2, 3, 4, 5, 6, 7, 8]]
))

# refer to: https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.html#plotly.graph_objects.layout.XAxis
# One of the following enumeration values:[‘-‘, ‘linear’, ‘log’, ‘date’, ‘category’, ‘multicategory’] 
fig.update_layout(xaxis_type="linear", yaxis_type="log", title='对数曲线')
#fig.show()

# -------------------------------------------------------------------------------------------------------
#  下面代码换用Dash的dcc.graph来展示上面生成的figure对象
# -------------------------------------------------------------------------------------------------------

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
