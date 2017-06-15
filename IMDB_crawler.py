import urllib.request
import csv 
with open('movies_1.csv', 'r') as csvfile: 
    links = list(csv.reader(csvfile, delimiter=','))
from bs4 import BeautifulSoup
import requests, sys, time
from random import randint
for x in range(1, len(links)):
    url = "http://www.imdb.com/title/tt" + links[x][3]
    headers = {'User-Agent':'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.98 Safari/537.36 Vivaldi/1.6.689.40'}
    req = urllib.request.Request(url = url, headers=headers)
    page = urllib.request.urlopen(req)
    content = page.read()
    sp = BeautifulSoup(content, 'html.parser')
    director = sp.find('span', {'class':'itemprop','itemprop':'name'})
    base = sp.find('span', {'class':'small'})
    movie = sp.find('div', {'class':'title_wrapper'})
    lst = []
    for node in movie.findAll('h1'):
        lst.append(''.join(node.findAll(text=True)))    
    rating_w = sp.find('span', {'itemprop':'ratingValue'}, {'class':'small'})
    rating_n = sp.findAll('div', {'class':'notEnoughRatings'})
    rating_n1 = sp.find('div', {'class':'notEnoughRatings'})
    if rating_n == []:
        print(links[x][0] + ";" + links[x][3] + ";" + lst[0] + ";" + director.string + ";" + rating_w.string + ";" + base.string)
    elif rating_n == []:
        print(links[x][0] + ";" + links[x][3] + ";" + lst[0] + ";" + director.string + ";" + rating_n.string + ";" + base.string)
    else:
        print(links[x][0] + ";" + links[x][3] + ";" + lst[0] + ";" + director.string + ";" + rating_n1.string + ";" + rating_n1.string)
    x+=1
    time.sleep(randint(3,10))
