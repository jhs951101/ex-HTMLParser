import requests
import urllib.request
import ssl
import os
from bs4 import BeautifulSoup

targetUrl = "url"
getpage= requests.get(targetUrl)
getpageSoup= BeautifulSoup(getpage.text, 'html.parser')
allClassTopsection= getpageSoup.findAll('img', attrs={'alt':'no image'})

for para1 in allClassTopsection:
    print(para1.text)
    print(str(para1))
    #boardLink = 'https://www.gimpo.go.kr/portal/' + str(para1).split('href="')[1].split('"')[0].replace('&amp;','&')[2:]

    #if not os.path.isdir(resultFolder):
            #os.makedirs(resultFolder)

    #htmlParser2 = HTMLParser(boardLink, 'div', {'class':'p-photo__wrap'})  # image saver

    #for para2 in htmlParser2:
        #imgLink = 'https://www.gimpo.go.kr' + str(para2).split('src="')[1].split('"')[0]
        #urllib.request.urlretrieve(imgLink, resultFolder + title + '.png')
