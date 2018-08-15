import urllib.request
from bs4 import *
from newspaper import Article
import re
from geotext import GeoText
import os

url='https://www.noticebard.com'

def get_links(page):
    page=urllib.request.urlopen(url).read().decode('utf-8')
    soup=BeautifulSoup(page,'lxml')
    tags = soup('a')
    s=[]
    for i in tags:
        if re.search('https',str(i)) == None:
            continue
        else:
            s.append(i.get('href'))
    return s


s=get_links(url)

# print(s)

# for i in s:
#     # print("i",i)
#     ns=get_links(i)
#     for j in ns:
#         s.append(j)
#         # if str(j) in s:
#         #     continue
#         # else:
#         #     print(i)
#         #     s.append(j)
# #
# for i in s :
    # print(i)

for k in s:
    print("k",k)
    art=Article(str(k),language="en")
    art.download()
    art.parse()
    art.nlp()
    # print(art.publish_date)
    # print(BeautifulSoup(urllib.request.urlopen("https://www.google.com"),"lxml").title.string)
    print("title",art.title)
    print(art.text)
    print(art.summary)
    # places = GeoText(art.text)
    # print(places.cities)
    soup_page=BeautifulSoup("https://www.noticebard.com/un-climate-change-video-competition-2018/",'lxml')
    tag_page=soup_page('h')
    print("h \n")
    for i in tag_page:
        print(i)
    print("\n\n")


os.system('spd-say "your program has finished"')
