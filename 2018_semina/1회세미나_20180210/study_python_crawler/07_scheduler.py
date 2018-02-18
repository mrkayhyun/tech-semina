# 일정 시간동안 주기적으로 돌아 가는 스케줄러 예제
# Author : DongHyun Kim
# Write Date : 2018-02-10

#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib
from bs4 import BeautifulSoup

from apscheduler.schedulers.blocking import BlockingScheduler

import smtplib
from email.mime.text import MIMEText

def getUrlData():
    fp = urllib.urlopen('https://www.clien.net/service/board/jirum')
    source = fp.read()
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')

    jirum_list = soup.find_all(attrs={'class': 'list_item symph_row'})



    for idx, jl in enumerate(jirum_list):
        jl_category = jl.find(attrs={'class': 'category'}).get_text()
        jl_title = jl.find(attrs={'data-role': 'list-title-text'}).get_text()
        findStr("하이마트", jl_title)
        sendMail(jl_title.encode("utf-8"))

def findStr(findStr, originStr):
    if findStr in originStr:
        print "일치"
        return True
    else:
        return False

def sendMail(mailContent):
    smtp = smtplib.SMTP('smtp.naver.com', 587)
    smtp.ehlo()  # say Hello
    smtp.starttls()  # TLS 사용시 필요
    smtp.login('test@naver.com', '')

    msg = MIMEText(mailContent)
    msg['Subject'] = mailContent
    msg['From'] = 'test@naver.com'
    msg['To'] = 'test@naver.com'
    smtp.sendmail('test@naver.com', 'test@naver.com', msg.as_string())

    smtp.quit()

sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=10)
def timed_job():
    print "timed_job excute!!"
    getUrlData()

sched.start()


