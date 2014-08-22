from bs4 import BeautifulSoup
import urllib2
url = "en.wikipedia.org/wiki/ISO_3166-1"
r = urllib2.urlopen("http://" +url)
soup = BeautifulSoup(r)
#tables = soup.findAll("table")
#i want to fetch data of india and store in a variable
t = soup.find("table")
for t1 in t.find_all('tr'):
    for cell in t1.find_all('td'):
       print cell.find_all(text=True)
        #cells = t.find_all('td',text="India")
  

