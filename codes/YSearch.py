from yahooboss import BossSearch

class YSearch(object):

    def __init__(self, key, secret_secret, max_results=50, result_age=10):
        self.key = key # your OATH2 key issued by Yahoo
        self.secret_key = secret_secret # your OATH2 secret_key issued by Yahoo
        self.age = result_age # maximum age of results default 10 days
        self.results_per_page = max_results # maximum number of results per page/request default 50 results
        pass
    
    def fetchYahooURLs(self, term):
        """ this method returns a generator of urls containing %results_per_page%
            results for query %term% issued on YahooBoass API """ 
        bs = BossSearch(self.key, self.key_secret, age=self.age,
                        results_per_page=self.results_per_page)
        web_results = bs.search_web(term)
        for wr in web_results:
            yield wr.get('url')
            pass
