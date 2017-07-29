from __future__ import print_function
from HTMLParser import HTMLParser  
from urllib2 import Request, urlopen
from urlparse import urljoin

class LinkFinder(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    newUrl = urljoin(self.baseUrl, value)
                    self.links = self.links + [newUrl]

    def getLinks(self, url):
        self.links = []
        self.baseUrl = url
        response = urlopen(url)
        try:
            htmlBytes = response.read()
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return list(set(self.links))
        except Exception as e:
            print(e)
            return []

def spider(url, maxPages):
    parser = LinkFinder()
    for link in parser.getLinks(url=url):
        print(link)

## running ...
spider(url="http://eu.battle.net/wow/en/", maxPages=20)
