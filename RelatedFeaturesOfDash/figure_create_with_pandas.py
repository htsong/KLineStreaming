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

#
# 第一步：读取链接上的pandas.DataFrame对象
#

# https://github.com/htsong/AppliedDataScience/blob/master/datasets/dataset_wine.csv
url = 'https://raw.githubusercontent.com/htsong/AppliedDataScience/master/datasets/dataset_wine.csv'
df = pd.read_csv(url) 
print(df.shape)

#
# 第二步：生成Figure对象
#
fig = px.scatter(df, x='alcohol', y='ash')  #y='target'


#
# 第三步：在网页上显示Figure对象
#

# 方法1： 直接用在网页上显示图片不做WEB应用
# fig.show()

# 方法2： 用Dash做个WEB应用
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])
app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
