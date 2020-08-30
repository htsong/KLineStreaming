#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# https://plotly.com/python/creating-and-updating-figures/
# 注意： 在Plotly中，fig是核心对象。下面是三种独立的生成fig对象的方法，测试时请分别放在单独的 .py 程序中进行

#
# 方法1：由字典输出图
# 
fig = dict({
    "data": [{"type": "Bar",
              "x":[20/(24*60), 1/24, 8/24, 1, 2, 6, 31],
              "y":[0.58, 0.44, 0.36, 0.34, 0.28, 0.25, 0.21] }],
    "layout": {"title": {"text": "A Figure of Specified By Python Dictionary"}}
})

# To display the figure defined by this dict, use the low-level plotly.io.show function
import plotly.io as pio
pio.show(fig)

#
# 方法2：graph_objects 对象输出图
#
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=[20/(24*60), 1/24, 8/24, 1, 2, 6, 31],
    y=[0.58, 0.44, 0.36, 0.34, 0.28, 0.25, 0.21]
))

#fig.add_trace(go.Scatter(
#    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
#    y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
#))

fig.update_layout(xaxis_type="log", yaxis_type="log", title='艾宾浩斯遗忘曲线')
fig.show()


#
# 方法3：Pandas对象和 plotly.express 联用
#
import pandas as pd
import plotly.express as px
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 title="Conditionally Updating Traces In A Plotly Express Figure With for_each_trace()")

fig.for_each_trace(
    lambda trace: trace.update(marker_symbol="square") if trace.name == "setosa" else (),
)
fig.show()
