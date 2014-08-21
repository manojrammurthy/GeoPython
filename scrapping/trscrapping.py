from bs4 import BeautifulSoup
import urllib2
url = "en.wikipedia.org/wiki/ISO_3166-1"
r = urllib2.urlopen("http://" +url)

soup = BeautifulSoup(r)
final_link = soup.p.a
final_link.decompose()

trs = soup.find_all('tr')
for tr in trs:
    print tr
    
    tds = tr.find_all("td")
    for td in tds:
        print td