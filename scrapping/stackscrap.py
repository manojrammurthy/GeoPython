import requests
from bs4 import BeautifulSoup
session = requests.session()


def fetchCode(country):
    page = session.get('http://en.wikipedia.org/wiki/ISO_3166-1')
    soup = BeautifulSoup(page.text).find('table', {'class': 'wikitable'})
    tablerows = soup.findAll('tr')
    for tr in tablerows:
        td = tr.findAll('td')
        if td:
            if td[0].text.lower() == country.lower():
                numeric_code = td[3].text
                ISO_code = td[4].text
                return numeric_code,ISO_code



var,var1=fetchCode(raw_input('Enter Country Name:'))
print var,var1