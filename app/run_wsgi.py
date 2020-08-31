#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://flask.palletsprojects.com/en/1.1.x/patterns/appdispatch/, 《Flask Application Dispatching》
# https://dash.plotly.com/integrating-dash

# https://pypi.org/project/Werkzeug/
from werkzeug.middleware.dispatcher import DispatcherMiddleware    # v1.01 <= from werkzeug.serving import run_simple
from werkzeug.serving import run_simple

from index import flask_app 
from get_kline_data import flask_app as get_kline_app
from show_kline_graph import app as show_kline_dash

application = DispatcherMiddleware(flask_app, {
    '/get_kline': get_kline_app,
    '/show_kline': show_kline_dash.server
})

if __name__ == '__main__':
    # https://werkzeug.palletsprojects.com/en/1.0.x/serving/
    run_simple(
        'localhost',   # 如果在网络访问，要绑定在0.0.0.0 
        8050, 
        application, 
        threaded=True  # 注意，如果不开启多线程支持，页面间互访就会一直超时！！！
    )
