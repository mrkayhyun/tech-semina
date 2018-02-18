# 원하는 url의 html을 가져와서 특정 부분의 html 리스트는 배열에 담아서 출력하는 예제
# Author : DongHyun Kim
# Write Date : 2018-02-10

# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib
from bs4 import BeautifulSoup


fp = urllib.urlopen('https://www.clien.net/service/board/jirum')
source = fp.read()
fp.close()

soup = BeautifulSoup(source, 'html.parser')

jirum_list = soup.find_all(attrs={'class': 'list_item symph_row'})



for idx, jl in enumerate(jirum_list):
    jl_category = jl.find(attrs={'class': 'category'}).get_text()
    jl_title = jl.find(attrs={'data-role': 'list-title-text'}).get_text()
    print "["+str(idx)+"]"
    print "카테고리 : "+jl_category
    print "제목 : " + jl_title
