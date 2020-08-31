#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://dash.plotly.com/integrating-dash
# http://tushare.org/trading.html#id2
import tushare as ts
from flask import Flask

# refer to: https://www.jianshu.com/p/0f528c47c5bf, 《Flask基本框架》
flask_app = Flask(__name__)

@flask_app.route('/')
def get_kline():
    df_50etf = ts.get_hist_data('510050') #一次性获取全部日k线数据
    return df_50etf.to_csv()

'''
if __name__ == '__main__':
    flask_app.run(debug=True, port=8050)
'''
