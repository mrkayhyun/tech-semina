# flask를 이용해서 url을 만들고 bs4를 통해서 가져온 데이터를 html의 형태로 출력하는 예제
# Author : DongHyun Kim
# Write Date : 2018-02-10

#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask
app = Flask(__name__)


import urllib
from bs4 import BeautifulSoup

def getUrlData():
    fp = urllib.urlopen('https://www.clien.net/service/board/jirum')
    source = fp.read()
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')

    jirum_list = soup.find_all(attrs={'class': 'list_item symph_row'})

    resultStr = '<!DOCTYPE html>'
    resultStr += '<head>'
    resultStr += '<meta charset="UTF-8">'
    resultStr += '</head>'
    resultStr += '<body>'

    resultStr += '<ul>'
    for idx, jl in enumerate(jirum_list):
        jl_category = jl.find(attrs={'class': 'category'}).get_text()
        jl_title = jl.find(attrs={'data-role': 'list-title-text'}).get_text()
        resultStr += "<li>["+str(idx)+"]"
        resultStr += "카테고리 : "+jl_category
        resultStr += "제목 : " + jl_title
        resultStr += "</li>"
        findStr("하이마트", jl_title)


    resultStr += '</ul>'
    resultStr += '</body>'
    resultStr += '</html>'

    return resultStr

# 원하는 문자열이 포함되어 있는지 검사
def findStr(findStr, originStr):
    if findStr in originStr:
        print "일치"
        return True
    else:
        return False

@app.route('/')
def getJirum():
    return getUrlData()

if __name__ == '__main__':
    app.run()