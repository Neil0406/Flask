from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from datetime import datetime
import csv
res = requests.get('https://rate.bot.com.tw/xrt?Lang=zh-TW')
soup = bs(res.text,'lxml')

def dtime():
    return datetime.today().strftime('%H:%M')


def tb():
    final_list = []

    data = soup.select('.print_show')
    r = []
    for i in data:
        r.append(i.text.split())
    for i in r:
        dic = {}
        dic['幣別'] = i[0]
        final_list.append(dic)
    #現買
    data = soup.select('#ie11andabove > div > table > tbody > tr > td:nth-child(2)')
    count = 0
    for i in data:
        final_list[count]['現金買價'] = i.text
        count += 1
    #現賣
    data = soup.select('#ie11andabove > div > table > tbody > tr > td:nth-child(3)')
    count = 0
    for i in data:
        final_list[count]['現金賣價'] = i.text
        count += 1
    #即期買
    data = soup.select('#ie11andabove > div > table > tbody > tr > td:nth-child(4)')
    count = 0
    for i in data:
        final_list[count]['即期買價'] = i.text
        count += 1
        
    #即期賣
    data = soup.select('#ie11andabove > div > table > tbody > tr > td:nth-child(5)')
    count = 0
    for i in data:
        final_list[count]['即期賣價'] = i.text
        final_list[count]['時間'] = dtime() 
        count += 1

    return final_list

