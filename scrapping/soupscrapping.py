from bs4 import BeautifulSoup
#import requests
import urllib2
#url = raw_input('enter a website to extract the url from')
url = "en.wikipedia.org/wiki/ISO_3166-1"
r = urllib2.urlopen("http://" +url)

soup = BeautifulSoup(r)
final_link = soup.p.a
final_link.decompose()
#print soup.prettify()
#print title
for link in soup.find_all('a'):
    print(link.get('href'))
