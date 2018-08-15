import urllib.request
from bs4 import *
from newspaper import Article
import re
from geotext import GeoText
url='https://timesofindia.indiatimes.com'

page=urllib.request.urlopen(url).read().decode('utf-8')

#text = html2text(page)
soup=BeautifulSoup(page,'lxml')                #make BeautifulSoup
#pr=soup.prettify()
#print(soup)
tags = soup('a')
#print(tags) while have the full tag
#f = open("out.txt","wb")
s=[]
for i in tags:
    s.append(i.get('href'))
    #f.write(i.get('href','utf-8'))
    #print(i.get('href')) # will show only the http wala link
#f.close()

ns=[]
pattern=r'(^https://timesofindia)'
'''for i in s:
    if(re.search(pattern,str(i))):
        ns.append(i)
        print(i)

'''
ns.append("http://www.rediff.com/rss/inrss.xml")
for i in ns:
    art=Article(str(i),language="en")
    art.download()
    art.parse()
    print(i)
    print(art.publish_date)
    print(art.text)
    places = GeoText(art.text)
    print(places.cities)
    print("\n\n")
'''
#for tag in tags:
    #print(tag.get('href',None))
'''
