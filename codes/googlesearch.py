from __future__ import print_function
import string
import sys
import re
import time
import requests
import urllib
import collections
import time
import random

# random time slice to send the queries to google
TSLICES = [9.3, 2.35, 3.4, 1.45, 5.0, 5.5, 7.6, 2.65, 5.7, 5.75, 10.8, 9.3, 2.85, 3.6, 1.8, 5.4, 5.1, 3.9, 2.75, 3.7, 13.75, 3.0]

class search_google(object):

    def __init__(self):
        self.server = "www.google.com"
        self.headers = {"User-Agent" : "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"}
        self.quantity = "100"
  
    def _do_search(self, term, start=0):
        try:
            urly="http://" + self.server + "/search?num=" + "100" + "&start=" + str(start) + "&hl=en&meta=&q=" + urllib.quote_plus(term)
        except Exception as e:
            print (e)
            return []
        else:
            try:
                r = requests.get(urly, headers=self.headers)
            except Exception as e:
                print (e)
                return []
            else:
                raw_results = r.text
                url_results = []
                r = re.findall('href="/url\?q=(.+?)">', raw_results, flags=re.I)
                for item in r:
                    if 'webcache.googleusercontent.com' not in item:
                        nr = re.findall('(.+)&amp;sa=U', item, flags=re.I)
                        if len(nr) > 0:
                            url_results.append(nr[0].strip())
                return url_results
        return []

class GoogleSearch(search_google):
    
    def _getURLs(self, term, num_results):
        results = []
        quotient = ((num_results/100) + 1)
        for x in xrange(0, quotient):
            ts = random.choice(TSLICES)
            time.sleep(ts)
            results += self._do_search(term, start=x*100)
        results = set(results)
        if len(results) <= num_results:
            return list(results)
        else:
            return list(results)[:num_results]

    def fetchURLs(self, term, num_results, output_file=None):
        urls = self._getURLs(term, int(num_results))
        if len(urls) > 0:
            if output_file:
                with open(output_file, "w") as outf:
                    for search_result in urls:
                        outf.write(search_result+"\n")
            else:
                return urls
        else:
            return []

if __name__ == "__main__":
    search = GoogleSearch()
    c = 0
    res = search.fetchURLs(term="sorrow", num_results=172, output_file=None)
    for i in res:
        c += 1
        print(i, c)
