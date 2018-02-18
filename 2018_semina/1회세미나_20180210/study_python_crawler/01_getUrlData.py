# 원하는 url의 html을 가져오는 예제
# Author : DongHyun Kim
# Write Date : 2018-02-10

# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup

fp = urllib.urlopen('https://www.clien.net/service/board/jirum')
source = fp.read()
fp.close()

soup = BeautifulSoup(source, 'html.parser')

print soup