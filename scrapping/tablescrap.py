from bs4 import BeautifulSoup
import urllib2
url = "en.wikipedia.org/wiki/ISO_3166-1"
r = urllib2.urlopen("http://" +url)
soup = BeautifulSoup(r)
#tables = soup.findAll("table")

t = soup.find("table")
for t1 in t.find_all('tr'):
    for cell in t1.find_all('td'):
        print cell.find_all(text=True)
    #cells = t.find_all('td',text="India")
    #rn = cells[0].get_text()
#print cells
#soup.find_all('a')
#title = soup.a
#title
