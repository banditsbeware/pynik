import requests

import os
from dotenv import load_dotenv
load_dotenv()
WORDNIK_KEY = os.getenv('WORDNIK_KEY')

class Words:
    
    # initialize with your api key
    def __init__(self, api_key):
        self.base = 'http://api.wordnik.com/v4'
        self.key = api_key

    # basic url builder for the words.json endpoint
    def get(self, command, args=[]):
        url = f'{self.base}/{command}?'
        for arg in args:
            url += arg + '&'
        url += f'api_key={self.key}'
        return requests.get(url)

        # a list of n random words
    def random(self, n=0):
        if n < 0: raise ValueError('Words.random(n): n must be zero or a positive integer')
        if n:
            json = self.get('words.json/randomWords', [f'limit={n}']).json()
            return [json[i]['word'] for i in range(n)]
        else:
            return self.get('words.json/randomWord').json()['word']

    def define(self, word):
        json = self.get(f'word.json/{word}/definitions').json()
        return json[0]['text']

if __name__ == '__main__':
    words = Words(WORDNIK_KEY)
    print(words.random(10))
    w = words.random()
    print(f'{w}: {words.define(w)}')

