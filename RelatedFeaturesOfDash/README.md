# Dash相关特性的演示程序

**需求简述**
---
先梳理一下需要的特性，主要有三方面：
* 一是绘制K线图，最好是多周期的可切换的K线图；
* 二是用户与K线图可动态交互，实现交易和数据查看；
* 三是K线数据随时间推移可以实时更新，最好是不要有页面刷新抖动。


**Dash简介**
---
[Dash](https://dash.plotly.com/)是一个用于构建基于 Web 的应用程序的 Python 库，无需 JavaScript 。

Dash 同时也是用于创建分析 Web 应用程序的用户界面库，希望使用 Python 进行数据分析、数据挖掘、可视化、
建模、仪器控制和报告的人可以立即使用 Dash 。

Dash 建立在 Plotly.js、React 和 Flask 之上，将现代 UI 元素（如下拉列表、滑块和图形）与你的分析 Python 代码相结合。


**Demo程序清单**
---
+ 用Plotly创建和更新网页图表

[Plotly](https://dash.plotly.com/dash-core-components/graph)是用来在网页上创建和渲染图形的python包，渲染过程是通过Plotly.js库实现的。

Python用户可以通过Dict或[plotly.graph_objects.Figure](https://plotly.com/python-api-reference/plotly.graph_objects.html)类实现图形操纵，而不用直接与下层的JS库打交道。

Plotly的图形也可通过JSON序列化为文本和保存。

Plotly还封装了[Plotly Express](https://plotly.com/python/plotly-express/)接口，提供了一组用于创建图形的简洁、一致的高级API。

原始文档参见：[Creating and Updating Figures with Plotly's Python graphing library](https://plotly.com/python/creating-and-updating-figures/)
+ 绘制K线图和参数调整
+ Dash多页WEB应用


**用Plotly创建和更新网页图表**
---
+ [JSON 与 Dict 相互转换](https://github.com/htsong/KLineStreaming/blob/master/RelatedFeaturesOfDash/transform_json_dict.py)
+ [用Plotly创建图形对象fig](https://github.com/htsong/KLineStreaming/blob/master/RelatedFeaturesOfDash/figure_create_with_plotly.py)
