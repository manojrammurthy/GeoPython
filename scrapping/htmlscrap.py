from HTMLParser import HTMLParser
import requests
import re

class MyHTMLParser(HTMLParser):

    data = []

    def handle_data(self, data):
        if re.findall('[a-zA-Z-:]', data):
            self.data.append(data)

if __name__ == '__main__':        

    url = 'http://en.wikipedia.org/wiki/ISO_3166-1'
    rsp = requests.get(url)

    p = MyHTMLParser()

    p.feed(rsp.text)

    s = p.data[p.data.index('Afghanistan'):p.data.index('ISO 3166-2:ZW')+1]

    name = raw_input('please input country name: ')
    print s[s.index(name)+3] 