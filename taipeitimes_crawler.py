from datetime import datetime
from dateutil.relativedelta import relativedelta
start = datetime.strptime("2017/01/01", "%Y/%m/%d")
month_list = []
for i in range(0,5):
    month_list.append((start + relativedelta(months=i)).strftime('%Y/%m/%d'))
def news(a):
    import urllib.request
    from bs4 import BeautifulSoup
    import requests, sys, time
    from random import randint

    month_url = "http://www.taipeitimes.com/News/main/history/"+a
    month_headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    month_req = urllib.request.Request(url = month_url, headers = month_headers)
    month_page = urllib.request.urlopen(month_req)
    month_content = month_page.read()
    month_sp = BeautifulSoup(month_content, 'html.parser')
    day_list_h = []
    for d in month_sp.find_all('tr', {'class':'date'}):
        day_list_h.append(d)
    month_sp1 = BeautifulSoup(str(day_list_h), 'html.parser')
    day_list = []
    for d1 in month_sp1.find_all('a'):
        day_list.append(d1.get('href'))
    contexts = []
    contexts_list = []
    for i in range(len(day_list)):
        day_url = "http://www.taipeitimes.com/"+day_list[i]
        day_headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        day_req = urllib.request.Request(url = day_url, headers = day_headers)
        day_page = urllib.request.urlopen(day_req)
        day_content = day_page.read()
        day_sp = BeautifulSoup(day_content, 'html.parser')
        for c in day_sp.find_all('div', {'class':'list_areaH'}):
            contexts.append(c)
        day_sp1 = BeautifulSoup(str(contexts), 'html.parser')
        for c1 in day_sp1.find_all('a'):
            contexts_list.append(c1.get('href'))
    tag2 = []
    news_text = []
    for i in range(len(contexts_list)):
        con_url = "http://www.taipeitimes.com/"+contexts_list[i]
        con_headers = {'User-Agent':'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.98 Safari/537.36 Vivaldi/1.6.689.40'}
        con_req = urllib.request.Request(url = con_url, headers=con_headers)
        con_page = urllib.request.urlopen(con_req)
        con_content = con_page.read()
        con_sp = BeautifulSoup(con_content, 'html.parser')
        tag = []
        news = []
        for t in con_sp.find_all('div', {'class':'etitle_c1'}):
            tag.append(t)
        con_sp2 = BeautifulSoup(str(tag), 'html.parser')
        for t2 in con_sp2.find_all('a'):
            tag2.append(t2.string)
        for n in con_sp.find_all('div', {'class':'text'}):
            news.append(n)
            con_sp3 = BeautifulSoup(str(news), 'html.parser')
            news_text.append(con_sp3.get_text())
            news_text = [s.strip('[\n') for s in news_text]
            news_text = [s.strip('\n]') for s in news_text]
            time.sleep(randint(2,10))
    return tag2, news_text
    
#month_list[0] January, month_list[0] February ...
tag2_1, news_text_1 = news(month_list[0])
news_dict1={"Type":tag2_1,"Content":news_text_1}
import pandas as pd
news_df1 = pd.DataFrame(news_dict1)
news_df1.to_csv('news1.csv')
