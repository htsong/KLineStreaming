#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask

# refer to: https://www.jianshu.com/p/0f528c47c5bf, 《Flask基本框架》
flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return "This is index page."

'''
if __name__ == '__main__':
    flask_app.run(debug=True, port=8050)
'''
