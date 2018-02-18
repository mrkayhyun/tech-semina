# flask 프레임워크의 hello 프로젝트 예제
# Author : DongHyun Kim
# Write Date : 2018-02-10

#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()