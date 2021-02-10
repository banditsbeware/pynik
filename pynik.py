import requests

WORDNIK_KEY = 'wdm3ufsvtmthan3w5xrrvr1nmpzkhh5n7wz4kher6uzfiuwtk'

class Words:
    
    # initialize with your api key
    def __init__(self, api_key):
        self.base = 'http://api.wordnik.com/v4'
        self.key = api_key

    # basic url builder for the words.json endpoint
    def get(self, command, args=[]):
        url = f'{self.base}/words.json/{command}?'
        for arg in args:
            url += arg + '&'
        url += f'api_key={self.key}'
        return requests.get(url)

    # one random word
    def random(self):
        json = self.get('randomWord').json()
        return json['word']

    # a list of n random words
    def randomWords(self, n):
        json = self.get('randomWords', [f'limit={n}']).json()
        return [json[i]['word'] for i in range(n)]


if __name__ == '__main__':
    words = Words(WORDNIK_KEY)
    # print(words.random())
    print(words.randomWords(10))

