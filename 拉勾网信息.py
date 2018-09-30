import requests
from bs4 import BeautifulSoup
import time
import pandas
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud ,ImageColorGenerator#词云
import PIL
from os import path
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
}
proxies = {'http': 'http://14.118.253.140:6666'}
message = []
for j in ['java','C','PHP','HTML5','python']:
    for p in range(1,60):
        time.sleep(1)
        url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%B9%BF%E4%B8%9C&kw='+j+'&p='+str(p)+'&sm=0&isfilter=0&fl=548&isadv=0&sb=1'
        html = requests.get(url,headers=headers).text
        jods = re.findall(r'target="_blank"><b>(.*?)</a>',html)
        companys = re.findall(r'<td class="gsmc"><a href=.*? target="_blank">(.*?)</a>',html)
        moneys = re.findall(r'<td class="zwyx">(.*?)</td>',html)
        places = re.findall(r'<td class="gzdd">(.*?)</td>',html)
        for jod,company,money,place in zip(jods,companys,moneys,places):
            if len(jod.replace('</b>',''))>12:
                continue
            print(j,jod.replace('</b>',''),company,money,place)
            message.append((j,jod.replace('</b>',''),company,money,place))
def save_message(message):
    # data = pandas.DataFrame(message,columns=['职位','地点','工资','经验'])
    # data.to_excel('test.xlsx',sheet_name='拉勾网数据',index=False)
    with open('test.txt', 'a') as f:
        for i in message:
            for j in i:
                f.write(j + '  ')
    f.close()

# save_message(message)
data = pandas.DataFrame(message,columns=['语言','职位','公司','工资','城市'])
data.to_excel('数据爬取.xlsx',sheet_name='招聘网网数据',index=False)






